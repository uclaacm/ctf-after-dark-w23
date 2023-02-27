const express = require('express');
const path = require('path');

const multer = require('multer');
const bodyParser = require('body-parser');

const port = parseInt(process.env.PORT) || 8080;

const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('app.db', sqlite3.OPEN_READONLY);

const app = express();
const upload = multer();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(upload.array());
app.use(express.static('public'));

const getFavColor = async (username) => {
    return new Promise((resolve, reject) => {
        db.get('SELECT fav_color FROM users WHERE username=?', username, (err, row) => {
            if (err) return resolve(err);
            return resolve(row.fav_color);
        });
    });
};

const attemptLogin = (username, password) => {
    return new Promise((resolve, reject) => {
        db.get(`SELECT username, password FROM users WHERE username='${username}'`, async (err, row) => {
            if (err)
                return reject(err);
            else if (row === undefined)
                return reject('Invalid User');
            else if (password === row.password)
                return resolve(`My favorite color is ${await getFavColor(row.username)}`);
            else
                return reject('incorrect password');
        });
    })
};

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'login.html'));
});

app.post('/', async (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    if (!username || !password)
        return res.status(400).send("Invalid Login");

    try {
        return res.status(200).send(await attemptLogin(username, password));
    } catch (err) {
        return res.status(400).send(err);
    }
});

app.get('*', (req, res) => {
    res.status(404).send('not found');
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
