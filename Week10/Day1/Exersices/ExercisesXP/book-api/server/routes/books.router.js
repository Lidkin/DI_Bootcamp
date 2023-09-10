const express = require('express');
const { getAllbooks, getBook, createBook } = require('../controllers/books.controllers.js');

const books_router = express.Router();

books_router.get('', getAllbooks);
books_router.get('/:id', getBook);
books_router.post('', createBook);

module.exports = books_router;