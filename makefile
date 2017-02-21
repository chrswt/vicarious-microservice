VIRTUALENV = $(shell which virtualenv)

venv:
	$(VIRTUALENV) venv

install:
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch:
	. venv/bin/activate; python services/translation.py

test:
	.	venv/bin/activate; python tests/translation.py