import './App.css';
import Tasks from './Tasks';
import { useState } from 'react';

function App() {

  const [todoList, setTodoList] = useState([{ id: 1, task: 'Finish homework' }]);

  const deleteTask = (id) => {
    const todos = todoList.filter(item => item.id != id);
    console.log(todos, id, todoList[id - 1].id)
    setTodoList(todos);
  }

  const addTask = (task) => {
    const id = todoList.length !== 0 ? todoList[todoList.length - 1].id + 1 : 1;
    const newTask = { id, task };
    const todos = [...todoList, newTask];
    setTodoList(todos);
  }

  return (
    <div className="App">
      <h1>Todo's</h1>
      <Tasks deleteTask={deleteTask} addTask={addTask} todoList={todoList} />
    </div>
  );
}

export default App;