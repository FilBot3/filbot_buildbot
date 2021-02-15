.PHONY: run-master logs venv

run-master:
	rm master/twistd.log
	buildbot start master

logs:
	cat master/twistd.log

venv:
	python -m venv venv/buildbot

