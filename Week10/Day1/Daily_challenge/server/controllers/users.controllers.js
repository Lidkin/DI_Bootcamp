const { _register, _login, _allUsers, _getUser, _putUser } = require('../models/users.models.js');
const bcrypt = require('bcrypt');
const saltRounds = 10;

const register = async (req, res) => {
    try {
        const { firstname, lastname, email, password } = req.body;
        const hash = await bcrypt.hash(password, saltRounds);
        const data = await _register({ firstname, lastname, email, password: hash });
        res.status(201).json(data);
    } catch (error) {
        console.log(error);
    }
}

const login = async (req, res) => {
    try {
        const { firstname, lastname, password } = req.body;
        const hash = await _login({ firstname, lastname, password });
        const data = await bcrypt.compare(password, hash);
        if (!data) return res.status(200).json({ msg: "User is not registered" });
        res.status(200).json({ msg: "Welcome back!"});
    } catch (error) {
        console.log(error)
    }
}

const allUsers = async (req, res) => {
    try {
        const data = await _allUsers();
        res.status(200).json(data);
    } catch (error) {
        console.log(error);
    }
}

const getUser = async (req, res) => {
    try {
        const id = req.params.id;
        const data = await _getUser(id);
        if (!data) return res.status(404).json({ msg: "No such user" });
        res.status(200).json(data);
    } catch (error) {
        console.log(error);
    }
}

const putUser = async (req, res) => {
    try {
        const {firstname, lastname, email } = req.body;
        const id = req.params.id;
        const data = await _putUser({ firstname, lastname, email }, id);
        res.status(200).json(data);
    } catch (error) {
        console.log(error);
    }
}

module.exports = { register, login, allUsers, getUser, putUser };
