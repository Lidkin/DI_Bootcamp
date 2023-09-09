const express = require('express');
const dotenv = require('dotenv');
const { posts } = require('./config/db.js');
dotenv.config();

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.listen(process.env.PORT);

// GET / posts: Return a list of all blog posts.
app.get('/api/blog/posts', (req, res) => {
    try {
        res.status(200).json(posts);
    } catch (err) {
        console.log(err);
    }
});

// GET /posts/:id: Return a specific blog post based on its id.

app.get('/api/blog/posts/:id', (req, res) => {
    try {
        const id = req.params.id;
        const post = posts.find(el => el.id == id);
        if (!post) return res.status(404).json({ msg: "post don't found" });
        res.status(200).json(post);
    } catch (err) {
        console.log(err);
    }
});

// POST /posts: Create a new blog post.

app.post('/api/blog/posts', (req, res) => {
    try {
        const { title, content } = req.body;
        const newPost = { id: posts.length + 1, title, content };
        posts.push(newPost);
        res.status(200).json(posts);
    } catch(err) {
        console.log(err);
    }
});

// PUT /posts/:id: Update an existing blog post.

app.put('/api/blog/posts/:id', (req, res) => {
    try {
        const { id } = req.params;
        const { title, content } = req.body;
        const index = posts.findIndex(el => el.id == id);
        posts[index] = { ...posts[index], title: title, content: content };
        res.status(200).json(index === -1 ? { msg: "no find any match" }:posts);
    } catch(err) {
        console.log(e);
    }
});

// DELETE / posts /: id: Delete a blog post.

app.delete('/api/blog/posts/:id', (req, res) => {
    try {
        const { id } = req.params;
        const index = posts.findIndex(el => el.id == id);
        if (index === -1) return res.status(404).json({ msg: "not found" });
        posts.splice(index, 1);
        res.status(200).json(posts);
    } catch (err) {
        console.log(err);
    }
});
