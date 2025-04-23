format:
	uv run ruff format
	uv run ruff check --fix

lint:
	uv run ruff check app/ --fix
	uv run mypy app/

test:
	uv run pytest

migrate:
	echo("WIP")

run:
	echo("WIP")
