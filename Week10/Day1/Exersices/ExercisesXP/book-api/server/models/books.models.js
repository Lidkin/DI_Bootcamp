const db = require('../config/db.js');

const _getAllbooks = () => {
    return db('books')
        .select('title', 'author', 'publishedyear');
};

const _getBook = (id) => {
    return db('books')
        .select('id', 'title', 'author', 'publishedyear')
        .where({ id });
};

const _createPost = ({ title, content }) => {
    return db('posts')
        .insert({ title, content }, ['title', 'content']);
};

const _createBook = ({ title, author, publishedyear }) => {
    console.log(title, author, publishedyear)
    return db('books')
        .insert({ title, author, publishedyear }, ['title', 'author', 'publishedyear']);
};

module.exports = { _getAllbooks, _getBook, _createBook };