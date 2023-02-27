FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir Flask gunicorn

WORKDIR /

COPY app.py app.py

COPY templates/ templates/

COPY static/ static/

USER 1000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "app:app"]