#/bin/bash

docker build -t rory/injection-perfection .
docker run -d --restart unless-stopped -p 10678:8080 rory/injection-perfection
