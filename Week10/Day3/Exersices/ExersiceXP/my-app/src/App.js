import './App.css';
import Car from './Components/Car.js';
import Event from './Components/Events.js';
import Phone from './Components/Phone';
import Color from './Components/Color';

function App() {
  const carinfo = { name: "Ford", model: "Mustang" }; 
  
  return (
    <div className="App">
      <Car car={carinfo} />
      <Event />
      <Phone />
      <Color />
    </div>
  );
};

export default App;
