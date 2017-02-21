VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr pig_latin_microservice.egg-info
	rm -fr venv
	rm -fr build
	rm -fr dist

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py -q install
	. venv/bin/activate; python setup.py -q develop

launch: venv shutdown
	. venv/bin/activate; python services/translation.py

test:
	. venv/bin/activate; python tests/translation.py

shutdown:
	ps -ef | grep 'services/translation.py' | grep -v grep | awk '{print $$2}' | xargs kill