// import express.js
const express = require("express");
const cookieParser = require("cookie-parser");

// create express app
const app = express();

// define port
const port = 3000;

const secret = 39;
const flag = "flag{c00k135_g0_brrr}";

// server static files
app.use(express.static("static"));
app.use(cookieParser());

// define route

// define challenge route
app.get("/flag", (req,res) => {
  if(Number(req.cookies.secret) === secret && Number(req.cookies.secret) < 250)
    res.send(flag);
  else
    res.send("icky cookie");  
});

// listen for requests
app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});