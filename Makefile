# start services attached to stdout
start:
	docker-compose -f local.yml up --build

# start services detached from stdout
run:
	docker-compose -f local.yml up -d --build

# stop all
stop:
	docker-compose -f local.yml stop

# make migrations
makemigrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations

# run Django migration file
migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate

# create Django admin user
create-admin:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

# run tests
test:
	docker-compose -f local.yml run --rm django pytest -s

# run tests with coverage
coverage:
	docker-compose -f local.yml run --rm django coverage run -m pytest

# view coverage report
coveragereport:
	docker-compose -f local.yml run --rm django coverage report

# create a new app
startapp:
	mkdir baskin_robbins/$(app) && django-admin startapp $(app) baskin_robbins/$(app)
