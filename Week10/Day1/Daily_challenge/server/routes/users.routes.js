const express = require('express');
const { register, login, allUsers, getUser, putUser } = require('../controllers/users.controllers.js');

const users_router = express.Router();

users_router.post('/register', register);
users_router.post('/login', login);
users_router.get('/users', allUsers);
users_router.get('/user/:id', getUser);
users_router.put('/user/:id', putUser);

module.exports = users_router;