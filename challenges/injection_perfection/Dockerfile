FROM node:19-bullseye-slim

WORKDIR /app
COPY . /app

RUN npm ci

RUN node /app/serialize.js
RUN chmod 444 app.db 

EXPOSE 8080
CMD ["node", "/app/index.js"]
