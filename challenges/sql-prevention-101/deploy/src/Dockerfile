FROM python:3.10-slim-bullseye
RUN apt-get update \
    && apt-get -yy install libmariadb3 \
    && apt-get -yy install libmariadb-dev

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

WORKDIR /app

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]