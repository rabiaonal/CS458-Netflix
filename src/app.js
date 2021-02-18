const http = require('http');
const fs = require('fs');
const express = require('express');

// Parse URL-encoded bodies (as sent by HTML forms)
const app = express();
app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended : true }));

const hostname = '127.0.0.1';
const port = 3000;

const users_file = 'users.json';
const users = JSON.parse(fs.readFileSync(users_file));

//Index page
app.get('/', function (req, res)
{
    res.render('index');
});

//Signup page
app.get('/signup', function (req, res)
{
    res.render('signup');
});

app.post('/signup', function (req, res)
{
    let user = { Email: req.body.email, Phone: req.body.phone, Password: req.body.password };

    var result;
    if(user.Phone.length == 0) result = checkUserData(user.Email, null, null);
    else result = checkUserData(user.Email, user.Phone, null);
    if(result.status == UserMatchStatus.INVALID_USER)
    {
        users.push(user);
        fs.writeFile(users_file, JSON.stringify(users), (err) =>
        {
            if(err) throw err;
        });
        res.redirect('home', { email: user.Email, phone: user.Phone });
    }
    else if(result.email != null)
    {
        res.render('signup', { alert: true, message: "Bu e-posta ile ilişkilendirilmiş bir hesap zaten var. Lütfen oturum açmayı deneyin."});
    }
    else
    {
        res.render('signup', { alert: true, message: "Bu telefon numarası ile ilişkilendirilmiş bir hesap zaten var. Lütfen oturum açmayı deneyin."});
    }
});

//Login page
app.get('/login', function (req, res)
{
    res.render('login');
});

app.post('/login', function (req, res)
{
    var result;
    if(emailOrPhone(req.body.email)) result = checkUserData(req.body.email, null, req.body.pass);
    else result = checkUserData(null, req.body.email, req.body.pass);
    if(result.status == UserMatchStatus.MATCH_SUCCESS)
    {
        res.render('home', { email: result.email, phone: result.phone });
    }
    else if(result.status == UserMatchStatus.INVALID_PASSWORD)
    {
        res.render('login', { alert: true, message: "Parola yanlış. Lütfen tekrar deneyin ya da parolanızı sıfırlayın."});
    }
    else
    {
        res.render('login', { alert: true, message: "Böyle bir hesap bulamadık. Lütfen kaydolmayı deneyin."});
    }
});

//Forgot password page
app.get('/forgotpassword', function (req, res)
{
    res.render('forgotpassword', {message: ''});
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});

const UserMatchStatus = {
    INVALID_USER : 0,
    INVALID_PASSWORD : 1,
    MATCH_SUCCESS : 2
};

function checkUserData(email, phone, password)
{
    for(var i = 0; i < users.length; i++)
    {
        if(users[i].Email == email)
        {
            if(users[i].Password == password)
            {
                return { email: users[i].Email, phone: users[i].Phone, status: UserMatchStatus.MATCH_SUCCESS };
            }
            return { email: users[i].Email, phone: null, status: UserMatchStatus.INVALID_PASSWORD };
        }
        if(users[i].Phone == phone)
        {
            if(users[i].Password == password)
            {
                return { email: users[i].Email, phone: users[i].Phone, status: UserMatchStatus.MATCH_SUCCESS };
            }
            return { email: null, phone: users[i].Phone, status: UserMatchStatus.INVALID_PASSWORD };
        }
    }
    return { email: null, phone: null, status: UserMatchStatus.INVALID_USER };
}

function emailOrPhone(input)
{
    return /[^\d.+()]+/.test(input);
}