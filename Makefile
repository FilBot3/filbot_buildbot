.PHONY: start-master start-worker logs venv start
.PHONY: stop stop-worker stop-master
.PHONY: restart restart-master restart-worker

venv:
	python -m venv venv/buildbot

start: start-master start-worker

start-master:
	rm master/twistd.log
	buildbot start master

start-worker:
	rm worker-local/twistd.log
	buildbot-worker start worker-local

stop: stop-master stop-worker

stop-master:
	buildbot stop master

stop-worker:
	buildbot-worker stop worker-local

restart: restart-master restart-worker

restart-master:
	buildbot restart master

restart-worker:
	buildbot-worker restart worker-local
