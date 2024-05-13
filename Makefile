.PHONY: add-lib
add-lib:
	poetry add $(filter-out $@,$(MAKECMDGOALS))

.PHONY: add-lib-dev
add-lib-dev:
	poetry add $(filter-out $@,$(MAKECMDGOALS)) --group dev

.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: qa
qa:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m src.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m src.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python -m src.manage runserver

.PHONY: shell
shell:
	poetry run python -m src.manage shell

.PHONY: superuser
superuser:
	poetry run python -m src.manage createsuperuser

.PHONY: test
test:
	poetry run coverage run -m src.manage test

.PHONY: test-coverage
test-coverage: test
	poetry run coverage report

.PHONY: test-cover-html
test-cover-html: test
	poetry run coverage html

.PHONY: update
update: install migrate install-pre-commit ;