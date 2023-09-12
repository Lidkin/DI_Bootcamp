import './App.css';
import { useState } from 'react';

function App() {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaSript", votes: 0 },
    { name: "Java", votes: 0 }
  ]);

  const voteFunc = (i) => {
    const arr = [...languages]
    arr[i].votes += 1;
    const vote = setLanguages(arr);
    return vote;
  }

  return (
    <div className="App">
      <h1>Vote your Language!</h1>
      <div className='languages'>
        {languages.map((item, i) => { return <div className='block'><div>{item.votes}</div><p>{item.name}</p><button key={i} onClick={() => voteFunc(i)}>Click Here</button><br /></div> })}
      </div>
    </div>
  );
}

export default App;
