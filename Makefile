format:
	uv run ruff format
	uv run ruff check --fix

lint:
	uv run ruff check --fix
	uv run mypy .

test:
	uv run pytest

migrate:
	echo("WIP")

run:
	echo("WIP")
