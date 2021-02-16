const http = require('http');
const fs = require('fs');
const express = require('express');

// Parse URL-encoded bodies (as sent by HTML forms)
app.use(express.urlencoded());

const hostname = '127.0.0.1';
const port = 3000;


let rawdata = fs.readFileSync('users.json');
let data = JSON.parse(rawdata);
console.log(data);

const server = http.createServer((req, res) => {

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    let path = "./";
    console.log(req.url);
    switch (req.url) {
        case "/":
            console.log(req.url);
            path += "index.html";
            break;
        case "/signup":
            path += "signup.html";
            break;
        case "/login":
            path += "login.html";
            break;
        case "/btnPressed":
            path += "login.html";
            break;
        default:
            res.statusCode = 404;
    }
    fs.readFile(path, (err,data) => {
        console.log(err);
        res.end(data)
    })
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});

