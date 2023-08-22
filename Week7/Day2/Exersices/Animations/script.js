
function hello() {
    alert('Hello World');
}

setTimeout(hello, 2000)

setTimeout(() => {
    const parag = document.createElement('p');
    parag.innerText = 'Hello World';
    container.appendChild(parag);
}, 2000)

function addPar() {
    const parag = document.createElement('p');
    parag.innerText = 'Hello World';
    container.appendChild(parag);
}

const interval = setInterval(() => {
    const parag = document.createElement('p');
    parag.innerText = 'Hello World';
    container.appendChild(parag);
    console.log(clear)
    clear.addEventListener('click', () => {
        clearInterval(interval)
    }
    )
}, 2000)


function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * letters.length)];
    }
    return color;
}

const child = document.getElementById("child");
function move(x, y) {
    child.style.left = x + "px";
    child.style.top = y + "px";
    child.style.backgroundColor = getRandomColor()

}
child.style.left = "0px";
let posX = 0;
let posY = 0;
let moveX = true;
let moveY = false;
let revers = false;
const intervalId = setInterval(() => {
    if (moveX && !revers) {
        posX += 10;
        if (posX === 300) {
            moveX = false;
            moveY = true;
        }
        move(posX, posY);
    } else if (moveY && !revers) {
        posY += 10;
        if (posY === 300) {
            moveY = false;
            revers = true;
        }
        move(posX, posY);
    } else if (!moveY && revers) {
        posX += -10;
        if (posX === 0) {
            revers = true;
            moveY = true;
        }
        move(posX, posY);
    } else if (moveY && revers) {
        console.log(posY)
        posY += -10;
        if (posY === 0) {
            clearInterval(intervalId);
        }
        move(posX, posY);
    } 
}, 100);