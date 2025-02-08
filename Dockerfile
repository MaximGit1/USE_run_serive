FROM python:3.12-slim

RUN pip install poetry==1.7.0

WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/app/src"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY ./src ./src

CMD ["poetry", "run", "python", "-m", "src.run.main"]