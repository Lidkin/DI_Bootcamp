const bcrypt = require('bcrypt');
const saltRounds = 10;
const { usersDB, usersToDB } = require('../modules/wr.file.js');

const register = async (req, res) => {
    try {
        const users = await usersDB();
        const { firstname, lastname, email, username, password } = req.body;
        const userExists = users.some(user => user.username == username);
        if (userExists) return res.status(409).json({ msg: `${username} already exists` });
        const hashpwd = await bcrypt.hash(password, saltRounds);
        users.push({ id: users[users.length - 1].id + 1, firstname, lastname, email, username, password: hashpwd });
        await usersToDB(users);
        res.status(200).json({ msg: `Hello ${username}, your accaunt is now created!` });
    } catch (error) {
        console.log(error);
    }
}

const login = async (req, res) => {
    try {
        const { username, password } = req.body;
        const users = await usersDB();
        const user = users.find(user => user.username == username);
        if (!user) return res.json({ msg: `${username} is not register` });
        const userPsw = await bcrypt.compare(password, user.password);
        if (!userPsw) return res.json({ msg: "wrong password" });
        res.status(200).json({ msg: `Hi ${username}, welcome back!` });
    } catch (error) {
        console.log(error);
    }
}

const allUsers = async (req, res) => {
    try {
        const users = await usersDB();
        res.status(200).json(users);
    } catch (error) {
        console.log(error);
    }
}

const getUser = async (req, res) => {
    try {
        const users = await usersDB();
        const id = req.params.id;
        const user = users.find(user => user.id == id);
        if (!user) return res.status(404).json("no sach user");
        res.status(200).json(user);
    } catch (error) {
        console.log(error);
    }
}

const putUser = async (req, res) => {
    try {
        const users = await usersDB();
        const id = req.params.id;
        const index = users.findIndex(user => user.id == id);
        if (index == -1) return res.status(500).json({ msg: "no such user" });
        const { firstname, lastname, email, username, password } = req.body;
        const hashpwd = await bcrypt.hash(password, saltRounds);
        const updUser = { firstname: firstname, lastname: lastname, email: email, username: username, password: hashpwd };
        users.splice(index, 1, updUser);
        await usersToDB(users);
        res.status(200).json({ msg: `${username}, your info was changed` });
    } catch (error) {
        console.log(error);
    }
}

module.exports = { register, login, allUsers, getUser, putUser };
