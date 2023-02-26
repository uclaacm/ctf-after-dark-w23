FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir Flask gunicorn redis

COPY ./src /app

WORKDIR /app
USER 1000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "app:app"]
