class TodoList {
    constructor() {
        this.task;
        this.listTasks = [];
    }

    addTask(task) {
        this.task = task;
        this.listTasks.push({ task: this.task, done: null });
    }

    markTask(task) {
        this.task = task;
        const findTask = this.listTasks.find(item => item['task'] == this.task && item['done'] == null);
        findTask['done'] = 'finished';
    }

    allTasks() {
        return this.listTasks;
    }
}

module.exports = TodoList;
