
install-dev-deps:
	poetry install

install-deps:
	poetry install --no-root --no-dev

server:
	cd src/ && poetry run alembic upgrade head && poetry run uvicorn app.main:app --reload --env-file .env

lint:
	poetry run flake8

isort:
	poetry run isort .

test:
	poetry run pytest --ff -x && poetry run pytest --dead-fixtures

coverage:
	cd src && poetry run pytest --dead-fixtures && poetry run pytest --cov-report=xml --cov=. -n4 -x

makemigrations:
	cd src && alembic revision --autogenerate

migrate:
	cd src && alembic upgrade head
