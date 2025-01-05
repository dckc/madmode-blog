# use .envrc to set DIIGO_USERNAME, DIIGO_API_KEY
SECRET_TOOL=secret-tool

diigo-bookmarks-shared.ndjson: diigo-bookmarks.ndjson
	jq -c 'select(.shared != "no")' <$< >$@

diigo-bookmarks.ndjson: diigo-bookmarks.json
	jq -c '.[]' <$< >$@

diigo-bookmarks.json: time-ref bkmkeep.py
	PASSWORD=$$($(SECRET_TOOL) lookup service diigo.com username $(DIIGO_USERNAME)) \
	python2 bkmkeep.py \
		$(DIIGO_USERNAME) PASSWORD DIIGO_API_KEY >$@ || (rm $@; exit 1)

time-ref:
	date -u -Iseconds >$@

time-reset:
	rm time-ref

install-deps:
	sudo apt install python2 jq libsecret-tools

guix-deps:
	guix shell less coreutils guix make python2 jq sqlite libsecret dbus nss-certs # --pure

q1: diigo-bookmarks-shared.ndjson bookmark-schema.sql
	sqlite3 :memory: -cmd '.read bookmark-schema.sql' \
		-cmd '.mode tabs' \
		-cmd '.import diigo-bookmarks-shared.ndjson bookmark_lines' \
		-cmd '.header on' -cmd '.mode column' \
		"select created_at, title, tags from bookmarks where tags like '%capabilit%'"
