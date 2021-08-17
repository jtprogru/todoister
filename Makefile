# Makefile сделан для упрощения некоторых действий

POETRY := ~/.poetry/bin/poetry
PROJECT_NAME := todoister
PROJECT_DESCRIPTION := "Простой проект в духе Todo https://github.com/jtprogru/todoister"
SERVER_HOST := 127.0.0.1
SERVER_PORT := 8000
LOG_LEVEL := debug
DEBUG := true
DATABASE_URI := sqlite:////tmp/todoister.sqlite
JWT_SECRET := "SuperSecretString0987654321"
MIGRATIONS_DATETIME := `date "+%Y-%m-%dT%H-%M-%S"`


default-env:
	@echo "Generate .env file"
	@echo "PROJECT_NAME=${PROJECT_NAME}\nPROJECT_DESCRIPTION=${PROJECT_DESCRIPTION}\n\nSERVER_HOST=${SERVER_HOST}\nSERVER_PORT=${SERVER_PORT}\n\nLOG_LEVEL=${LOG_LEVEL}\nDEBUG=${DEBUG}\n\nDATABASE_URI=${DATABASE_URI}\n\nJWT_SECRET=${JWT_SECRET}"> src/.env

install-dev-deps:
	${POETRY} install

install-deps:
	${POETRY} install --no-root --no-dev

server:
	cd src/ && ${POETRY} run alembic upgrade head && ${POETRY} run uvicorn app.main:app --reload --env-file .env

lint:
	${POETRY} run flake8

isort:
	${POETRY} run isort .

test:
	${POETRY} run pytest && ${POETRY} run pytest --dead-fixtures

coverage:
	cd src && ${POETRY} run pytest --dead-fixtures && ${POETRY} run pytest --cov-report=xml --cov=. -n4 -x

makemigrations:
	cd src && ${POETRY} run alembic revision --autogenerate -m "${MIGRATIONS_DATETIME}"

migrate:
	cd src && ${POETRY} run alembic upgrade head

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
