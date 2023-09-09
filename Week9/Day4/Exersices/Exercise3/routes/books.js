const express = require('express');
const router = express.Router();

const books = [{ id: 1, author: "H. P. Lovecraft", title: "The Alchemist", datePublished: 1916}];

router.get('/books', (req, res) => {
    res.status(200).json(books);
});

router.post('/books', (req, res) => { 
    const id = books.length + 1;
    const newBook = {
        id: id,
        author: req.body.author,
        title: req.body.title,
        datePublished: req.body.datePublished
    };
    books.push(newBook);
    res.status(201).json(books);
});

router.put('/books/:id', (req, res) => {
    const id = req.params.id;
    const book = books.find(item => item.id == id);
    if (req.body.author) book.author = req.body.author;
    if (req.body.title) book.title = req.body.title;
    if (req.body.datePublished) book.datePublished = req.body.datePublished;
    res.status(200).json(book);
});

router.delete('/books/:id', (req, res) => {
    const id = req.params.id;
    const ind = books.findIndex(item => item.id == id);
    books.splice(ind, 1);
    res.status(200).json(books);
});

module.exports = router;