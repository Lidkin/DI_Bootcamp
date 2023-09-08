const ToDo = require('./todo.js');

const tasksList = new ToDo();
const tasks = ["Finish all exercises", "Go to sleep on time", "Read good book", "Finish all exercises"];
for(const task of tasks) {
    tasksList.addTask(task);
};
console.log(tasksList.allTasks());
tasksList.markTask(tasks[1]);
tasksList.markTask(tasks[0]);
console.log(tasksList.allTasks());
tasksList.markTask("Finish all exercises");
console.log(tasksList.allTasks());