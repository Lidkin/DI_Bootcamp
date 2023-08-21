// Using a DOM property, retrieve the h1 and console.log it.

console.log(document.querySelector('h1'));

// Using DOM methods, remove the last paragraph in the < article > tag.
const article = document.querySelector('article')
article.lastElementChild.remove();

// // Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

const h2 = document.querySelector('h2')
h2.addEventListener('click', () => {
    h2.style.backgroundColor = 'red'
});

// Add an event listener which will hide the h3 when it’s clicked on(use the display: none property).
const h3 = document.querySelector('h3')
h3.addEventListener('click', () => {
    h3.style.display = 'none'
});

// // Add a < button > to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

const but = document.createElement('button')
but.innerText = 'Bold'
// article.parentElement.append(button)
bold.appendChild(but)
but.addEventListener('click', () => {
    article.style.fontWeight = 'bold'
});

// // BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

const h1 = document.querySelector('h1')

h1.addEventListener('mouseover', () => {
    let size = Math.random() * 100;
    h1.style.fontSize = size + 'px'
})

// // BONUS: When you hover on the 2nd paragraph, it should fade out(Check out “fade css animation” on Google)


h2.addEventListener('mouseover', () => {
    h2.style.opacity = '50%';
    setTimeout(() => {
        h2.style.opacity = '100%';
    }, 5000);
})

//Exercise 2:

// Retrieve the form and console.log it.

console.log(document.querySelector('form'))

// Retrieve the inputs by their id and console.log them.
console.log(fname, lname, submit)

// Retrieve the inputs by their name attribute and console.log them.

console.log(document.getElementsByName('firstname'))
console.log(document.getElementsByName('lastname'))
console.log(document.getElementsByName('submit'))


document.querySelector('form').addEventListener('submit', function (event) {
    const userName = []
    event.preventDefault();
    userName.push(event.target.elements.firstname.value);
    userName.push(event.target.elements.lastname.value);
    const answers = document.getElementsByClassName('usersAnswer')[0];
    for (i in userName) {
        let word = i < 1 ? 'first' : 'last';
        const li = document.createElement('li');
        li.innerText = `${word} name of the user: ${userName[i]}`;
        answers.append(li);
    };
})


//Exercise 3:

let allBoldItems;
const parag = document.querySelector('ul').nextElementSibling;

function getBoldItems() {
    allBoldItems = document.querySelectorAll('strong');
    return allBoldItems;
}

function highlight() {
    getBoldItems().forEach(item => {
        item.style.color = 'blue';
    });
}

function returnItemsToDefault() {
    getBoldItems().forEach(item => {
        item.style.color = 'black';
    });
}

parag.addEventListener('mouseover', highlight);
parag.addEventListener('mouseout', returnItemsToDefault);

//Exercise 4:

myForm.volume.style.display = 'none';
myForm.addEventListener('submit', (event) => {
    event.preventDefault();
    let v = 4 / 3 * Math.PI * Math.pow(event.target.elements.radius.value, 3);
    console.log(event.target.elements)
    event.target.elements.volume.value = Math.round(v);
    myForm.volume.style.display = 'block';
    setTimeout(() => {
        myForm.volume.style.display = 'none';
     }, 3000);
});

//Exercise 5:

let experiment = document.createElement('button');
experiment.innerText = 'push';
experiment.style.fontWeight = 'bold';
experiment.style.margin = '10px 20px';
buttonE.appendChild(experiment);

experiment.addEventListener('mousedown', () => {
    experiment.innerText = 'push DOWN';
    experiment.style.color = 'turquoies';
    experiment.style.backgroundColor = 'blue';
    experiment.style.border = '2px solid gold';
    experiment.style.fontStyle = 'italic';
});
experiment.addEventListener('click', () => {
    experiment.innerText = 'push CLICK';
    experiment.style.border = '2px solid gold';
    experiment.style.fontStyle = 'normal';
    experiment.style.position = 'absolute';
    experiment.style.left = '30%'
    experiment.style.top = '30%'
});
experiment.addEventListener('dblclick', () => {
    let pos1 = 30, pos2 = 30;
    let i1, i2, i=-1;
    let sign = [1, 0, 0, 1, -1, 0, 0, -1];
    experiment.innerText = 'push DBCLICK';
    experiment.style.border = '2px solid gold';
    experiment.style.position = 'absolute';
    console.log(pos1, pos2)
    const interval = setInterval(() => {
        if (i < 4) {
            i++;
            experiment.style.left = pos1 + '%'
            experiment.style.top = pos2 + '%'
            experiment.style.backgroundColor = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`
            experiment.style.color = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;
            if (i <= 4) {
                if (i % 2 == 0) { i1 = i * 2; i2 = i * 2 + 1; }
                else { i1 = i * 2; i2 = i * 2 + 1 };
                pos1 += 20 * sign[i1];
                pos2 += 20 * sign[i2];
            }
        } else {
            clearInterval(interval);
        }
    }, 1000 )

});
experiment.addEventListener('mouseleave', () => {
    experiment.style.border = '2px dotted red';
});
