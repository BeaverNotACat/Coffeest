format:
	uv run ruff format
	uv run ruff check --fix

lint:
	uv run ruff check --fix
	uv run mypy .

test:
	uv run pytest

coverage:
	uv run coverage run -m pytest
	uv run coverage report -m

migrate:
	echo("WIP")

run:
	echo("WIP")
