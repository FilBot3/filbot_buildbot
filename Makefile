.PHONY: run-master

run-master:
	rm master/twistd.log
	buildbot start master

logs:
	cat master/twistd.log
