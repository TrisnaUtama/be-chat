FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install uv
RUN uv pip sync --no-cache-dir pyproject.toml

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]