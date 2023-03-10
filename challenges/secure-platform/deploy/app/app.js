// import express.js
const express = require("express");

// create express app
const app = express();

// define port
const port = 8041;

// server static files
app.use('/static', express.static("public"));

// define route
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

// define challenge route
app.get("/flag", (req, res) => {
  const platform = req.header("sec-ch-ua-platform");
  if(platform === '"INTEGRITY-178B"'){
    res.send(`<p>what a secure OS! of course you can have my flag!! <\p><p>flag{sh0uldv3_us3d_n4v1g4t0r}<\p>`);
  } else {
    res.send(`<p>Your platform isn't secure enough! I only like platforms with an EAL of 6 or higher.<\p><p>Your platform is ${platform}, I'd much rather it be "INTEGRITY-178B".<\p>`);
  }
});

// listen for requests
app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});
