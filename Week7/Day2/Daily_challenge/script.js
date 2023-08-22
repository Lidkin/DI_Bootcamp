
let arr = [];

const sentence = (a) => {
    let str = a.join(' ');
    return str.charAt(0).toUpperCase() + str.slice(1);
};

libform.addEventListener('submit', (event) => {

    event.preventDefault();

    for (let i = 0; i < 5; i++) {
        arr.push(event.target.elements[i].value);
    }

    story.innerText = sentence(arr) + '.';
});

shuffle.addEventListener('click', () => {

    let currentIndex = arr.length, randomIndex;
    while (currentIndex != 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [arr[currentIndex], arr[randomIndex]] = [
            arr[randomIndex], arr[currentIndex]];
    }

    story.innerText = sentence(arr) + '.';
});
