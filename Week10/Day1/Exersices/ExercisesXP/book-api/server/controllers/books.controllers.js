const books = require('../config/db.js');
const { _getAllbooks, _getBook, _createBook, _updateBook, _deleteBook } = require('../models/books.models.js');

const getAllbooks = async (req, res) => {
    try {
        const data = await _getAllbooks();
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "not found" });
    };
};

const getBook = async (req, res) => {
    try {
        const id = req.params.id;
        const data = await _getBook(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "not found" });
    };
};

const createBook = async (req, res) => {
    console.log(req.body)
    try {
        const data = await _createBook(req.body);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    };
};

module.exports = { getAllbooks, getBook, createBook };