FROM python:3.12.3-slim
WORKDIR /app
COPY pyproject.toml /app/
RUN pip install poetry
RUN poetry install --no-root
COPY . /app
ENV PYTHONUNBUFFERED=1
EXPOSE 5002
CMD ["poetry", "run", "python", "main.py"]