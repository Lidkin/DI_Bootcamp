import { useState } from "react";

function Events() {
    const [isToggleOn, setToggle] = useState(true);

    const clickMe = () => {
        alert('I was clicked');
    };



    const handleKeyDown = (event) => {
        if (event.key == 'Enter') alert(`The Enter key was pressed, your input is:  ${event.target.value}`);
    };

    return (
        <div>
            <button onClick={clickMe}>Click Me!</button>
            <input onKeyDown={handleKeyDown} placeholder="Press the ENTER key!"></input>
            <button onClick={() => setToggle(!isToggleOn)}>{ isToggleOn ? "ON" : "OFF" }</button>
        </div>
    )

}

export default Events;