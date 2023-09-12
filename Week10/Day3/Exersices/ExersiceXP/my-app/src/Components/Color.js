import { useState, useEffect } from "react";

function Color() {
    const [favoriteColor, setColor] = useState('red');

    useEffect(() => {
        console.log(favoriteColor)
        if (favoriteColor == 'red') {
            alert('useEffect reached');
            setColor('yellow');
        };
    }, [favoriteColor]);

    return (
        <>
            <h1>My Favorite Color is <i>{favoriteColor}</i></h1>
            <button onClick={() => setColor('blue')}>Change Color</button>
        </>
    );
}

export default Color;