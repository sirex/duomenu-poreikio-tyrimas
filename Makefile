.PHONY: run
run: env/bin/django-admin
	env/bin/python manage.py runserver

env/bin/django-admin: env/bin/python setup.py
	env/bin/pip install -e ".[tests]"

env/bin/python:
	python3 -m venv env
