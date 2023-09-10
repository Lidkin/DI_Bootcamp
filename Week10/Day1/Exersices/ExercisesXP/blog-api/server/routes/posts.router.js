const express = require('express');
const { getAllposts, getPost, createPost, updatePost, deletePost } = require('../controllers/posts.controllers.js');

const posts_router = express.Router();

posts_router.get('/', getAllposts);
posts_router.get('/:id', getPost);
posts_router.post('/', createPost);
posts_router.put('/:id', updatePost);
posts_router.delete('/:id', deletePost);

module.exports = posts_router;