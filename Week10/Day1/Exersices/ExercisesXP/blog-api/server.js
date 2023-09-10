const express = require('express');
const posts_router = require('./server/routes/posts.router');
require('dotenv').config();

const app = express();
app.use(express.json());

app.use('/api', posts_router);

app.listen(process.env.PORT);