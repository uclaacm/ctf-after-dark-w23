#/bin/bash

docker build -t rory/injection-perfection .
docker run --restart=always -p 10678:8080 rory/injection-perfection
