// import express.js
const express = require("express");

// create express app
const app = express();

// define port
const port = 3000;

// server static files
app.use('/', express.static("public"));

// listen for requests
app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});