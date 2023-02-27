FROM node:19-bullseye-slim

WORKDIR /app
COPY . /app

RUN npm ci

ENV FLAG=flag{red_is_the_best_color_fight_me_you_wont}
RUN node /app/serialize.js
RUN chmod 444 app.db 

EXPOSE 8080
CMD ["node", "/app/index.js"]
