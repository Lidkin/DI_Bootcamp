const express = require('express');
const users_router = require('./server/routes/users.routes.js');

require('dotenv').config();

const app = express();

app.use(express.json());
app.use('', users_router);

app.listen(process.env.PORT, console.log(process.env.PORT));