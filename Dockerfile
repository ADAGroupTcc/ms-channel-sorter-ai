FROM python:3.10-slim AS build
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y gcc

# Copiar arquivos do projeto
COPY pyproject.toml poetry.lock ./
COPY . .

# Instalar Poetry
RUN pip install poetry

# Instalar dependências do projeto
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Expor a porta da aplicação
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
