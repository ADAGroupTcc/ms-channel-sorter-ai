FROM python:3.10-slim AS build
WORKDIR /app

RUN apt-get update && apt-get install -y gcc

COPY pyproject.toml poetry.lock ./
COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry lock && poetry install --no-dev

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
