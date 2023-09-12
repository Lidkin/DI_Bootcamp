import { useState } from "react";
import Garage from './Garage.js';

function Car(props) {
    const [color, setColor] = useState('red');

    return (
        <header>
            <h2>This car is {color} {props.car.model} </h2>
            <Garage size="small" />
        </header>
    );
};

export default Car;