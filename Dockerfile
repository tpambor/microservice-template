FROM python:3.12-slim

COPY . /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD ["hypercorn",  "--bind", "0.0.0.0:8000", "app:create_app()"]
