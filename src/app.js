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


//TO DO
app.get('/signup', function (req, res)
{
    res.render('signup', {message: ''});
});

app.post('/signup', function (req, res)
{
    //	Bu hesap zaten var gibi görünüyor. İlgili hesapta oturum açın ya da farklı bir e‑posta adresi kullanmayı deneyin.
    var result = checkUserData(req.body.email, req.body.pass) ;

    if(result.status === "successful")
        res.render('signupsuccess', {name: result.name});
    else
        res.render('name', {message: result.status});
    console.log(req.body);
});



//Login page
app.get('/login', function (req, res)
{
    res.render('login', {message: ''});
});

app.post('/login', function (req, res)
{
    var result = checkUserData(req.body.email, req.body.pass) ;
    if(result.status === "successful")
        res.render('loginsuccess', {name: result.name});
    else
        res.render('login', {message: result.status});
    console.log(req.body);
});

//Forgot password page
app.get('/forgotpassword', function (req, res)
{
    res.render('forgotpassword', {message: ''});
});


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});

function checkUserData(email, password){
    var rawdata = fs.readFileSync('users.json');
    var users = JSON.parse(rawdata);

    for(var i = 0; i < users.length; i++){
        if(users[i].Email == email){
            if(users[i].Password == password){
                return {name: users[i].Name, status: "successful"};
            }
            return {name: "", status: "Parola yanlış. Lütfen yeniden deneyin ya da parolanızı sıfırlayın."};
        }
    }
    return {name: "", status: "Bu e‑posta adresi ile bağlantılı bir hesap bulamadık. Lütfen yeniden deneyin ya da yeni bir hesap oluşturun."};
}