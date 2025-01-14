dev:
	poetry run python main.py

services-up:
	docker compose -f src/infra/compose.yaml up -d

test:
	poetry run pytest

lint-ruff-check: 
	poetry run ruff check

lint-ruff-fix: 
	poetry run ruff check --fix

format-ruff-check: 
	poetry run ruff format --check

format-ruff-fix:
	poetry run ruff format

typecheck-pyright:
	poetry run pyright

