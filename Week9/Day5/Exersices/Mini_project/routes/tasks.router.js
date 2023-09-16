const express = require('express');
const fs = require('fs');
const router = express.Router();
const path = require('path');
const tasksPath = path.join(__dirname, '..', 'config', 'tasks.json');

router.get('/tasks', (req, res) => {
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'));
    res.status(200).json(tasks);
});

router.get('/tasks/:id', (req, res) => {
    const id = req.params.id;
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'));
    const task = tasks.find(item => item.id == id);
    if (!task) return res.status(404).json({ msg: "no such task" });
    res.status(200).json(task);
});

router.post('/tasks', (req, res) => {
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'));
    const { task, mark } = req.body;
    const id = tasks.length > 0 ? tasks[tasks.length - 1]['id'] + 1 : 1
    tasks.push({ id, task, mark });
    fs.writeFileSync(tasksPath, JSON.stringify(tasks));
    res.status(201).json({ msg: "new task added" });
});

router.put('/tasks/:id', (req, res) => { 
    const id = req.params.id;
    const { task, mark } = req.body;
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'));
    const index = tasks.findIndex(item => item.id == id); 
    if (!index) return res.status(404).json({ msg: "no such task" });
    tasks.splice(index, 1, { id, task, mark });
    fs.writeFileSync(tasksPath, JSON.stringify(tasks));
    res.status(200).json(JSON.parse(fs.readFileSync(tasksPath, 'utf-8'))[index]);
});

router.delete('/tasks/:id', (req, res) => {
    const id = req.params.id;
    const tasks = JSON.parse(fs.readFileSync(tasksPath, 'utf-8'));
    const index = tasks.findIndex(item => item.id == id);
    if (!index) return res.status(404).json({ msg: "no sach task" });
    tasks.splice(index, 1);
    fs.writeFileSync(tasksPath, JSON.stringify(tasks));
    res.status(200).json(tasks);
});

module.exports = router;