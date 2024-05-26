# use .envrc to set DIIGO_USERNAME, DIIGO_API_KEY
SECRET_TOOL=secret-tool

diigo-bookmarks-shared.ndjson: diigo-bookmarks.ndjson
	jq -c 'select(.shared=="yes")' <$< >$@

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
