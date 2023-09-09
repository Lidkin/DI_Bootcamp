const express = require('express');
const dotenv = require('dotenv');
const fetchPosts = require('./data/dataService.js')
dotenv.config();

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.listen(process.env.PORT);

app.get('/posts', async (req, res) => {
    try {
        const postsData = await fetchPosts('https://jsonplaceholder.typicode.com/posts');
        res.status(200).json(postsData);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});