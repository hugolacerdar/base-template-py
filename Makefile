dev:
	poetry run python main.py

lint-ruff-check: 
	poetry run ruff check

lint-ruff-fix: 
	poetry run ruff check --fix