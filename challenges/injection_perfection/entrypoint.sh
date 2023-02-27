#/bin/bash

docker build -t rory/injection-perfection .
docker run -d -p 10678:8080 rory/injection-perfection
