const express = require('express');
const router = require('./routes/quiz.js');
const cors = require('cors');

const app = express();

app.use(express.json());
app.use(express.static('./game'))
app.use(cors({ origin: 'http://127.0.0.1:5500' }));
app.use(router);

app.listen(3000);
