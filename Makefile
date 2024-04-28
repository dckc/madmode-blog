# use .envrc to set DIIGO_USERNAME, DIIGO_API_KEY

diigo-bookmarks.json: time-ref bookmark-dl/bkmkeep.py
	python2 bookmark-dl/bkmkeep.py \
		$(DIIGO_USERNAME) DIIGO_PASSWORD DIIGO_API_KEY >$@

time-ref:
	date >$@

time-reset:
	rm time-ref

install-deps:
	sudo apt install python2
