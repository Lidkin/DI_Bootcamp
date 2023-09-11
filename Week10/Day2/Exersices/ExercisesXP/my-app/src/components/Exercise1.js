function Exercise1() {
    const paragraph = <p>Hello World!</p>;
    const myelement = <h1>I Love JSX!</h1>;
    const sum = 5 + 5;
    const text = `React is ${sum} times better with JSX`
    return (
        <div className="App">
            {paragraph}
            {myelement}
            <p>{text}</p>
        </div>
    );
};

export default Exercise1;