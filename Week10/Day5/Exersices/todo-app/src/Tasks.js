import { useState} from "react";

function Tasks(props) {

    const [task, setTask] = useState('');
  
    const handleFunc = (e) => { 
        e.preventDefault();
        if (e.target.localName === 'form') {
            props.addTask(task);
            setTask('');
        } else {
            const id = e.target.id;
            console.log(id)
            props.deleteTask(id);
        }

    }

    return (
        <div>
            <div>
                {props.todoList.length != 0 ?
                    props.todoList.map(item => {
                    return (<p onClick={(e) => {handleFunc(e) } } className="tasks" id={item.id} key={item.id}>{item.task}</p>)
                    }) : (<p id="empty">Your todo's list is empty!</p>)
                }
            </div>
            <form onSubmit={(e) => { handleFunc(e) }}>
                <label>Add a new todo:<input type='text' name='newtodo' value={task} onInput={(e) => { setTask(e.target.value) }} /></label>
            </form>
        </div>
    );

}

export default Tasks;