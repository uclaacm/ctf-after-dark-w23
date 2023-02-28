FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir flask mysql-connector-python

COPY . /app

WORKDIR /app

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]