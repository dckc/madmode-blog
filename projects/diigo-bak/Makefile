# use .envrc to set DIIGO_USERNAME, DIIGO_API_KEY
# optional retry tuning:
# DIIGO_REQUEST_TIMEOUT_SECONDS=15
# DIIGO_MAX_RETRIES=5
# DIIGO_RETRY_BASE_DELAY_SECONDS=1
# DIIGO_RETRY_MAX_DELAY_SECONDS=60
SECRET_TOOL=secret-tool

diigo-bookmarks-shared.ndjson: diigo-bookmarks.ndjson
	jq -c 'select(.shared != "no")' <$< >$@

diigo-bookmarks.ndjson: diigo-bookmarks.json
	jq -c '.[]' <$< >$@

diigo-bookmarks.json: time-ref bkmkeep.py
	PASSWORD=$$($(SECRET_TOOL) lookup service diigo.com username $(DIIGO_USERNAME)) \
	python2 bkmkeep.py \
		$(DIIGO_USERNAME) PASSWORD DIIGO_API_KEY >$@

time-ref:
	date -u -Iseconds >$@

time-reset:
	rm time-ref

install-deps:
	sudo apt install python2 jq libsecret-tools
