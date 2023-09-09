const greet = (name) => {
    const greetArr = ['Hello', 'Hi', 'Alloha', 'Good day'];
    const ind = Math.floor(Math.random() * greetArr.length);
    return `${greetArr[ind]}, ${name}!`;
};

export default greet;