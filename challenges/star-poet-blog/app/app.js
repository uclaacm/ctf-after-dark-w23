// import express.js
const express = require("express");

// create express app
const app = express();

// define port
const port = 3000;

// server static files
app.use('/', express.static("public"));

// define route
app.get("/hi", (req, res) => {
  res.send("Hello World!");
});

// define challenge route
app.get("/challenge/:word", (req, res) => {
  const word = req.params.word;
  if(word === "flag"){
    res.send("here's the flag");
  } else {
    res.send("Not the flag");
  }
});

// define /flag route
app.get("/flag", (req, res) => {
  res.send("here's the flag");
});

//define /cat route
app.get("/cat", (req, res) => {
  res.send("flag{cat}"); 
});

// listen for requests
app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});