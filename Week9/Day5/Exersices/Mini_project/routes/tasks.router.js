const express = require('express');
const fs = require('fs');
const router = express.Router();
const path = require('path');
const tasksPath = path.join(__dirname, '..', 'config', 'tasks.json');

router.get('/tasks', (req, res) => {
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'));
    res.status(200).send(tasks);
});

router.get('/tasks/:id', (req, res) => {
    const id = req.params.id;
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'));
    const task = tasks.find(item => item.id = id);
    if (!task) return res.status(404).json({ msg: "no such task" });
    res.status(200).json(task);
});

router.post('/tasks', (req, res) => { 
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'))
    const { task, mark } = req.body;
    tasks.push({ id: tasks.length + 1, task, mark });
    fs.writeFileSync(tasksPath, JSON.stringify(tasks));
    res.status(201).json({ msg: "new task added" });
})

module.exports = router;