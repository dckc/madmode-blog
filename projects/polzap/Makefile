# SPDX-License-Identifier: CC0-1.0
# Dump the phone's SMS/MMS provider to a file via adb content query.
SHELL := /bin/bash
FILTER_ADDR ?=

## Dump SMS from the phone (content://sms)
sms-dump.txt:
	adb shell content query --uri content://sms --projection _id,address,body,date > $@.tmp && mv $@.tmp $@

## Dump MMS + parts from the phone (content://mms)
sms-mms.txt:
	{ adb shell content query --uri content://mms --projection _id,date,sub,ct_t,ct_l; echo "---MMS_PARTS---"; adb shell "content query --uri content://mms/part --projection _id:mid:ct:text"; } > $@.tmp && mv $@.tmp $@

## Parse the dumps into a unified message list
msgs.json: sms-dump.txt sms-mms.txt
	python3 scripts/parse_sms.py --sms sms-dump.txt --mms sms-mms.txt > $@.tmp && mv $@.tmp $@

## Mirror the parsed dump into eval/
eval/msgs.json: msgs.json
	cp msgs.json $@

## Build the evaluation spreadsheet
eval/polzap-eval.xlsx: eval/msgs.json eval/labels.json
	python3 scripts/build_spreadsheet.py eval/msgs.json eval/labels.json $@

## Diff the current dump against the saved one
sms-dump.diff:
ifndef FILTER_ADDR
	$(error FILTER_ADDR is required)
endif
	diff <(python3 scripts/parse_sms.py --strip-row --filter-addr $(FILTER_ADDR) ,sv/sms-dump.txt) <(python3 scripts/parse_sms.py --strip-row --filter-addr $(FILTER_ADDR) sms-dump.txt)
