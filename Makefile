# ENV=$(HOME)/pyenv/mm
ENV=/usr/local/devtools/miniconda/envs/pydata1
PYTHON=$(ENV)/bin/python

STAGE=../dckc.github.io

build-gh-pages:
	(cd $(STAGE); rm -rf *)
	rm -rf build
	$(PYTHON) site build
	cp -r build/* $(STAGE)/
	(cd $(STAGE); git status)

.ipynb.md:
	$(ENV)/bin/jupyter-nbconvert --to markdown $<
	# $(PYTHON) static/code/ipynb_pub/mm_ipy.py $< $@

.PHONY: build

.SUFFIXES: .ipynb .md
