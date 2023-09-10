const posts = require('../config/db.js');
const { _getAllposts, _getPost, _createPost, _updatePost, _deletePost } = require('../models/posts.models.js');

const getAllposts = async (req, res) => {
    try {
        const data = await _getAllposts();
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "not found" });
    };
};

const getPost = async (req, res) => {
    try {
        const id = req.params.id;
        const data = await _getPost(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "not found" });
    };
};

const createPost = async (req, res) => {
    try {
        const data = await _createPost(req.body);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    };
};

const updatePost = async (req, res) => {
    console.log("put recieved")
    try {
        const id = req.params.id;
        const data = await _updatePost(req.body, id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

const deletePost = async (req, res) => {
    try {
        const id = req.params.id;
        const data = await _deletePost(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

module.exports = { getAllposts, getPost, createPost, updatePost, deletePost };