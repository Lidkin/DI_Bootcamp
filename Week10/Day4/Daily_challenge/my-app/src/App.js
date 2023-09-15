import './App.css';
import { useState } from 'react';
import FormComponent from './FormComponent.js';

function App() {

  const [inputs, setInputs] = useState({
    firstname: '',
    lastname: '',
    age: '',
    gender: '',
    destination: '',
    nutsFree: false,
    lactoseFree: false,
    vegan: false,
  });

  const handleChange = (e) => {
    console.log(e.target.textContent)
    const value = (e.target.type === 'checkbox') ? e.target.checked : e.target.value;
    setInputs({ ...inputs, [e.target.name]: value });
  }

  return (
    <div className="App">
      <header><h1>Sample form</h1></header>
      <form>
        <input type="text" placeholder="First Name" name="firstname" onInput={(e) => { handleChange(e) }} /><br />
        <input type="text" placeholder="Last Name" name="lastname" onInput={(e) => { handleChange(e) }} /><br />
        <input type="number" placeholder="Age" name="age" onInput={(e) => { handleChange(e) }} /><br /><br />
        <label><input type="radio" name="gender" value="female" onChange={handleChange} checked={inputs.gender === 'female'} />Female</label><br />
        <label><input type="radio" name="gender" value="male" onChange={handleChange} checked={inputs.gender === 'male'} />Male</label><br />
        <label>Select destination<br />
          <select name="destination" onChange={handleChange}>
            <option disabled selected>--Please Choose a destination--</option>
            <option>Tokyo</option>
            <option>London</option>
            <option>Vienna</option>
            <option>Milan</option>
          </select>
        </label><br></br><br></br>
        <fieldset>
          <legend>Dietary restrictions</legend>
          <label><input type="checkbox" name='nutsFree' onChange={(e) => { handleChange(e) }}></input>Nuts free</label><br/>
          <label><input type="checkbox" name='lactoseFree' onChange={(e) => { handleChange(e) }} />Lactose free</label><br />
          <label><input type="checkbox" name='vegan' onChange={(e) => { handleChange(e) }} />Vegan</label><br />
        </fieldset>

        <button type='submit'>Submit</button> 
      </form>
      {console.log(inputs)}
      <FormComponent inputs={inputs} />
    </div>
  );
}

export default App;
