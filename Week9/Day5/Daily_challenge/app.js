const express = require('express');
const router = require('./routes/users.routes.js')
const cors = require('cors');
const app = express();

app.use(express.json());
app.use(cors({ origin: 'http://127.0.0.1:5500' }));
app.use(express.static('./static'));

app.use(router);

app.listen(3000);