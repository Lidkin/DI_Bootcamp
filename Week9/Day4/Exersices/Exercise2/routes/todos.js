const express = require('express');
const router = express.Router();

const todos = [{id: 1, task: "read the book", mark: null}];

router.get('/todos', (req, res) => {
    res.status(200).json(todos);
});

router.post('/todos', (req, res) => {
    const newTask = {
        id: todos.length + 1,
        task: req.body.task,
        mark: req.body.mark
    };
    todos.push(newTask);
    res.status(201).json(todos);
});

router.put('/todos/:id', (req, res) => {
    const id = req.params.id;
    const task = todos.find(item => item.id == id);
    if (req.body.task) task.task = req.body.task;
    if (req.body.mark) task.mark = req.body.mark;
    res.status(200).json(task);
});

router.delete('/todos/:id', (req, res) => {
    const id = req.params.id;
    const ind = todos.findIndex(item => item.id == id);
    todos.splice(ind, 1);
    res.status(200).json(todos);
});

module.exports = router;
