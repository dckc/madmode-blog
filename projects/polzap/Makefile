# SPDX-License-Identifier: CC0-1.0
# Dump the phone's SMS/MMS provider to a file via adb content query.
SHELL := /bin/bash
FILTER_ADDR ?=

sms-dump.txt:
	adb shell content query --uri content://sms --projection _id,address,body,date > $@.tmp && mv $@.tmp $@

sms-mms.txt:
	{ adb shell content query --uri content://mms --projection _id,date,sub,ct_t,ct_l; echo "---MMS_PARTS---"; adb shell "content query --uri content://mms/part --projection _id:mid:ct:text"; } > $@.tmp && mv $@.tmp $@

msgs.json: sms-dump.txt sms-mms.txt
	python3 scripts/parse_sms.py --sms sms-dump.txt --mms sms-mms.txt > $@.tmp && mv $@.tmp $@

sms-dump.diff:
ifndef FILTER_ADDR
	$(error FILTER_ADDR is required)
endif
	diff <(python3 scripts/parse_sms.py --strip-row --filter-addr $(FILTER_ADDR) ,sv/sms-dump.txt) <(python3 scripts/parse_sms.py --strip-row --filter-addr $(FILTER_ADDR) sms-dump.txt)
