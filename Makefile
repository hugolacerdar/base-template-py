dev:
	poetry run python main.py

lint-ruff-check: 
	poetry run ruff check

lint-ruff-fix: 
	poetry run ruff check --fix

format-ruff-check: 
	poetry run ruff format --check

format-ruff-fix:
	poetry run ruff format