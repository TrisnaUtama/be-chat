dev :
	uv run uvicorn app.main:app --reload --port 8888

format: 
	uv run ruff format
	uv run ruff check --fix