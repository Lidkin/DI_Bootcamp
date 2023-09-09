const books = require('./config/db.js');
const express = require('express');
const dotenv = require('dotenv');
dotenv.config();

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.listen(process.env.PORT);

app.get('/api/books', (req, res) => {
    res.status(200).json(books);
});

app.get('/api/books/:bookId', (req, res) => {
    const id = req.params.bookId;
    const book = books.find(item => item.id == id);
    if (!book) return res.status(404).json({ msg: "no such book" });
    res.status(200).json(book);
});

app.post('/api/books', (req, res) => {
    const { title, author, publishedYear } = req.body;
    const id = books.length + 1;
    books.push({ id, title, author, publishedYear });
    res.status(201).json(books[id - 1]);
});
