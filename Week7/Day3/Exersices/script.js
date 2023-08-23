//Exercise 1

// #1
function funcOne() {
    let a = 5;
    if (a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
funcOne();
console.log('my answer is: 3')
// #1.2 What will happen if the variable is declared
// with const instead of let ?
console.log('will returned 5')

//#2
let a1 = 0;
function funcTwo() {
    a1 = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a1}`);
}

// #2.1 - run in the console:
funcThree()
console.log('my answer: 0');
funcTwo()
console.log('my answer: a1 = 5')
funcThree() // my answer: 5
console.log('my answer: 5')
// #2.2 What will happen if the variable is declared
// with const instead of let ?

console.log('a1 stay be 0')

//#3
function funcFour() {
    window.a1 = "hello";
}


function funcFive() {
    alert(`inside the funcFive function ${a1}`);
}

// #3.1 - run in the console:
funcFour()
funcFive()

//#4
let a2 = 1;
function funcSix() {
    let a2 = "test";
    alert(`inside the funcSix function ${a2}`);
}

// #4.1 - run in the console:
funcSix();
console.log('my answer: test');
// #4.2 What will happen if the variable is declared
// with const instead of let ?

console.log('error')

//#5
let a3 = 2;
if (true) {
    let a3 = 5;
    alert(`in the if block ${a3}`);
}
alert(`outside of the if block ${a3}`);

console.log('inside: 5, outside: 2')

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared
// with const instead of let ?



//Exersice 2

function winBattle() {
    return true;
};

let experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints);

//Exercise 3
const isString = (a) => typeof a === 'string' ? true : false;

console.log(isString('hello'));
//true
console.log(isString([1, 2, 4, 0]));
//false

//Exercise 4:
const sum = (x, y) => x + y;
console.log(sum(1, 2));

//Exercise 5:
function receive(kg) {
    return kg * 1000;
};

const kgToGr = function (kg) {
    return kg * 1000;
};

const kgGr = (kg) => kg * 1000;
console.log(receive(2), kgToGr(2), kgGr(2));
//Exercise 6:


((children, partner, location, job) => {
    const body = document.querySelector('body');
    let h1 = document.createElement('h1');
    h1.innerText = `You will be ${job.startsWith('a') ? 'an' : 'a'} ${job} in ${location}, and married to ${partner} with ${children} kids.`
    h1.style.textAlign = 'center';
    body.appendChild(h1)
})(5, 'Lola', 'France', 'artist');

//Exercise 7:

/*John has just signed in to your website and you want to welcome him.*/

(() => {
    const navB = document.querySelector('nav');
    console.log(navB)
    let div = document.createElement('div');
    div.style.display = 'flex';
    div.style.flexDirection = 'column';
    div.style.alignItems = 'center';
    div.innerHTML = `<p style="font-style: oblique">John</p> 
    <img src = "https://images.unsplash.com/photo-1624395213232-ea2bcd36b865?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NjN8fG1lbiUyMGZhY2V8ZW58MHwxfDB8fHwy&auto=format&fit=crop&w=600&q=60" style = "width:200px"></img>`;
    navB.appendChild(div);
})();

//Exercise 8:
//part I
const makeJuice = (size) => {
    let ingredients = [];
    const addIngredients = (ingr1, ingr2, ingr3) => {
        ingredients.push(ingr1, ingr2, ingr3);
    };
    const displayJuice = (ingredients) => {
        const body = document.querySelector('body');
        let par = document.createElement('p');
        const ingred = ingredients.reduce((acc, val) => `${acc},  ${val}`);
        par.innerText = `The client wants a ${size} juice, containing ${ingred}.`;
        body.appendChild(par);
    }
    addIngredients('vodka', 'berries', 'lime');
    addIngredients('orange', 'rum', 'melon');
    displayJuice(ingredients);
}

makeJuice('big');