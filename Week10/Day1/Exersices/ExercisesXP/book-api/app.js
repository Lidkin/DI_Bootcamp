const express = require('express');
const books_router = require('./server/routes/books.router.js');
require('dotenv').config();

const app = express();
app.use(express.json());

app.use('/api/books', books_router);

app.listen(process.env.PORT);