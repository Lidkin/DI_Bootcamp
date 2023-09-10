const db = require('../config/db.js');

const _getAllposts = () => {
    return db('posts')
        .select('id', 'title', 'content');
};

const _getPost = (id) => {
    return db('posts')
        .select('id', 'title', 'content')
        .where({ id });
};

const _createPost = ({ title, content }) => {
    return db('posts')
        .insert({ title, content }, ['title', 'content']);
};

const _updatePost = ({ title, content }, id) => {
    return db('posts')
        .update({ title, content })
        .where({ id })
        .returning(['id', 'title', 'content']);
};

const _deletePost = (id) => {
    return db('posts')
        .del()
        .where({ id })
        .returning(['id', 'title']);
};

module.exports = { _getAllposts, _getPost, _createPost, _updatePost, _deletePost };