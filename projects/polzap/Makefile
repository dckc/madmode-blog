# SPDX-License-Identifier: CC0-1.0
# Dump the phone's SMS provider to a file via adb content query.

sms-dump.txt:
	adb shell content query --uri content://sms --projection _id,address,body,date > $@
