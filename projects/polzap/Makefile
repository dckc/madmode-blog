# SPDX-License-Identifier: CC0-1.0
# Pull the phone's SMS/MMS provider and polzap's index DB into device/ via adb.
SHELL := /bin/bash
FILTER_ADDR ?=
DEVICE := device
APP_ID := madmode.polzap.smsfilter

## Dump SMS from the phone (content://sms)
$(DEVICE)/sms-dump.txt:
	mkdir -p $(DEVICE)
	adb shell content query --uri content://sms --projection _id,address,body,date > $@.tmp && mv $@.tmp $@

## Dump MMS + parts from the phone (content://mms)
$(DEVICE)/sms-mms.txt:
	mkdir -p $(DEVICE)
	{ adb shell content query --uri content://mms --projection _id,date,sub,ct_t,ct_l; echo "---MMS_PARTS---"; adb shell "content query --uri content://mms/part --projection _id:mid:ct:text"; } > $@.tmp && mv $@.tmp $@

## Parse the dumps into a unified message list
eval/msgs.json: $(DEVICE)/sms-dump.txt $(DEVICE)/sms-mms.txt
	mkdir -p eval
	python3 scripts/parse_sms.py --sms $(DEVICE)/sms-dump.txt --mms $(DEVICE)/sms-mms.txt > $@.tmp && mv $@.tmp $@

## Build the evaluation spreadsheet
eval/polzap-eval.xlsx: eval/msgs.json eval/labels.json
	python3 scripts/build_spreadsheet.py eval/msgs.json eval/labels.json $@

## Save the current SMS dump for a later sms-dump.diff
.PHONY: device-snapshot
device-snapshot: $(DEVICE)/sms-dump.txt
	mkdir -p $(DEVICE)/prev
	cp $(DEVICE)/sms-dump.txt $(DEVICE)/prev/sms-dump.txt

## Diff the current dump against the snapshot
sms-dump.diff:
ifndef FILTER_ADDR
	$(error FILTER_ADDR is required)
endif
	diff <(python3 scripts/parse_sms.py --strip-row --filter-addr $(FILTER_ADDR) $(DEVICE)/prev/sms-dump.txt) <(python3 scripts/parse_sms.py --strip-row --filter-addr $(FILTER_ADDR) $(DEVICE)/sms-dump.txt)

## Download polzap's Room DB (+ WAL/SHM sidecars) from the phone
# Room keeps recent writes in a write-ahead log, so the .db alone can look
# empty: copy the -wal/-shm sidecars too, then fold them in locally.
.PHONY: dl-db
dl-db:
	adb get-state  # fails unless the phone is connected and authorized
	mkdir -p $(DEVICE)
	for f in polzap_index.db polzap_index.db-wal polzap_index.db-shm; do \
	  rm -f $(DEVICE)/$$f; \
	  if adb shell run-as $(APP_ID) test -e databases/$$f; then \
	    adb exec-out run-as $(APP_ID) cat databases/$$f > $(DEVICE)/$$f; \
	  fi; \
	done
	head -c 15 $(DEVICE)/polzap_index.db | grep -q 'SQLite format 3' \
	  || { echo "$(DEVICE)/polzap_index.db is not a SQLite DB:" >&2; head -c 200 $(DEVICE)/polzap_index.db >&2; exit 1; }
	# fold the WAL into the local copy and leave it a single self-contained file
	sqlite3 $(DEVICE)/polzap_index.db "PRAGMA journal_mode=DELETE;" | grep -qx delete
	sqlite3 -header -column $(DEVICE)/polzap_index.db "SELECT count(*) AS messages, count(DISTINCT sender_identity) AS senders, datetime(min(intercept_timestamp)/1000, 'unixepoch', 'localtime') AS earliest, datetime(max(intercept_timestamp)/1000, 'unixepoch', 'localtime') AS latest FROM indexed_political_messages;"

## Count indexed political texts per month
.PHONY: db-monthly
db-monthly: dl-db
	sqlite3 -header -column $(DEVICE)/polzap_index.db "SELECT strftime('%Y-%m', intercept_timestamp/1000, 'unixepoch', 'localtime') AS month, count(*) AS messages FROM indexed_political_messages GROUP BY month ORDER BY month;"
