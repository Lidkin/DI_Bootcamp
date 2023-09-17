const express = require('express');
const { register, login, allUsers, getUser, putUser } = require('../controllers/users.controllers.js');

const router = express.Router();

router.post('/register', register);
router.post('/login', login);
router.get('/users', allUsers);
router.get('/user/:id', getUser);
router.put('/user/:id', putUser);

module.exports = router;