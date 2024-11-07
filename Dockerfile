FROM python:3.10-slim AS build
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--port", "80"]
