import { useState } from "react";

function Phone() {
    const [brand] = useState('Samsung');
    const [model] = useState('Galaxy S20');
    const [color, setColor] = useState('black');
    const year = useState(2020);

    return (
        <>
            <h2>My phone is a {brand}</h2>
            <p>It is a {color} {model} from {year}</p>
            <button onClick={() => setColor('red')}>Change color</button>
        </>
    );
};

export default Phone;