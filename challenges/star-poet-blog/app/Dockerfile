# Node.js v16 base image
FROM node:16

# Copies all of the local files into the container
COPY . /

# Installs dependencies
RUN npm install

# Exposes port 3000
EXPOSE 3000

# Runs the app
CMD [ "node", "app.js" ]