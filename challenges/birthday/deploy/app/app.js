// import express.js
const express = require("express");

// create express app
const app = express();

// define port
const port = 2500;

// server static files
app.use('/static', express.static("public"));

// define route
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.get("/cake.png", (req, res) => {
  res.sendFile(__dirname + "/public/cake.png");
});

app.get("/present.jpeg", (req, res) => {
  res.sendFile(__dirname + "/public/present.jpeg");
});

// listen for requests
app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});