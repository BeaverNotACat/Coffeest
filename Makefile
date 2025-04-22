format:
	uv run ruff format app/
	uv run ruff check app/ --fix

lint:
	uv run ruff check app/ --fix
	uv run mypy app/

test:
	echo("WIP")

migrate:
	echo("WIP")

run:
	echo("WIP")
