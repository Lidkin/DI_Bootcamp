const express = require('express');
const dotenv = require('dotenv');
const { randomEmoji, saveDataToFile, usersDb } = require('./modules/myModules.js');
const filePath = './config/users.json';
dotenv.config();

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static('../frontend'));

app.listen(process.env.PORT);

app.get('/api/emojis', (req, res) => {
    try {
        res.status(200).json({ randomEmoji });
    } catch (err) {
        console.log(err);
    };
});

app.post('/api/users', (req, res) => {
    try {
        const index = usersDb.length
        const { userName, score } = req.body;
        usersDb.push({ id: index + 1, userName, score });
        res.json(usersDb[index]);
        saveDataToFile(usersDb, filePath);
    } catch (err) {
        console.log(err);
    }
});

app.put('/api/users', (req, res) => {
    try {
        const user = req.body;
        usersDb.splice(user.id - 1, 1, user);
        res.json(usersDb[user.id - 1]);
        saveDataToFile(usersDb, filePath);
    } catch (err) {
        console.log(err);
    }
});

app.get('api/users', (req, res) => {
    try {
        const users = [...usersDb.sort((a, b) => a.score - b.score)];
        res.json(users);
    } catch (err) {
        console.log(err);
    }
})

app.get('/api/users/:id', (req, res) => {
    try {
        const id = req.params.id;
        const user = usersDb.find(user => user.id == id);
        if (!user) return res.status(200).json({ msg: "no sach user" });
        res.status(200).json(user);
    } catch (err) {
        console.log(err);
    }
});

app.get('/api/score', (req, res) => {
    try {
        const sortedArr = [...usersDb];
        sortedArr.sort((a, b) => b.score - a.score);
        res.status(200).json(sortedArr);
    } catch (err) {
        console.log(err);
    }
});