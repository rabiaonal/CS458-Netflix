const http = require('http');
const fs = require('fs');
const express = require('express');

// Parse URL-encoded bodies (as sent by HTML forms)
const app = express();
app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended : true }));

const hostname = '127.0.0.1';
const port = 3000;

let users = JSON.parse(fs.readFileSync('users.json'));
console.log(users);

app.get('/', function (req, res)
{
    res.render('index');
});

app.get('/login', function (req, res)
{
    res.render('login', {message: ''});
});

app.post('/login', function (req, res)
{
    for(i = 0; i < users.length; i++)
    {
        if(users[i].Email == req.body.email)
        {
            res.render('login', {message: 'login succesful'});
        }
    }
    res.render('login', {message: 'login failed'});
    console.log(req.body);
});

app.get('/signup', function (req, res)
{
    res.render('signup');
});

app.listen(port);

/**
const server = http.createServer((req, res) => {

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    let path = "./";
    console.log(req.url);
    switch (req.url) {
        case "/":
            console.log(req.url);
            path += "index.ejs";
            break;
        case "/signup":
            path += "signup.ejs";
            break;
        case "/login":
            path += "login.ejs";
            break;
        case "/btnPressed":
            path += "login.ejs";
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
 **/

