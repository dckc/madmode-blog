# use .envrc to set DIIGO_USERNAME, DIIGO_API_KEY
SECRET_TOOL=secret-tool

diigo-bookmarks.json: time-ref bookmark-dl/bkmkeep.py
	PASSWORD=$$($(SECRET_TOOL) lookup service diigo.com username $(DIIGO_USERNAME)) \
	python2 bookmark-dl/bkmkeep.py \
		$(DIIGO_USERNAME) PASSWORD DIIGO_API_KEY >$@

time-ref:
	date >$@

time-reset:
	rm time-ref

install-deps:
	sudo apt install python2
