console.log('Exercise 1:')

function displayNumbersDivisible(divisor) {
    let numbers = []
    let divNumbers = []
    var sum = 0
    for (let i = 0; i < 501; i++) {
        numbers.push(i)
    }
    numbers.forEach(number => {
        if (number % divisor == 0) {
            divNumbers.push(number)
            sum += number
        }
    });
    console.log(`Outcome : ${divNumbers.join(' ')} `)
    console.log(`Sum : ${sum}`)
}

displayNumbersDivisible(23)
displayNumbersDivisible(45)

console.log('Exercise 2:-------------------------')

const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

const shoppingList = ['banana', 'orange', 'apple']

function myBill(list, stock, prices) {
    let bill = 0
    list.forEach(item => {
        if (item in stock && stock[item] != 0) {
            bill += prices[item]
            stock[item] -= 1
        }
    });
    console.log(bill)
    console.log(stock)
}

myBill(shoppingList, stock, prices)

console.log('Exercise 3:--------------------------')
function changeEnough(itemPrice, amountOfChange) {
    quarters = 0.25 * amountOfChange[0]
    dimes = 0.10 * amountOfChange[1]
    nickel = 0.05 * amountOfChange[2]
    penny = 0.01 * amountOfChange[3]
    sum = quarters + dimes + nickel + penny
    result = sum >= itemPrice ? true : false
    console.log(result)
}

changeEnough(14.11, [2, 100, 0, 0]) // => returns false
changeEnough(0.75, [0, 0, 20, 5]) // => returns true

console.log('Exercise 4:--------------------------')
function hotelCost(userInput) {
    return 140 * userInput
}

function planeRideCost(userInput) {
    console.log(userInput)
    switch (userInput) {
        case 'London': return 183;
        case 'Paris': return 220;
        default: return 300;
    }
}

function rentalCarCost(userInput) {
    totalPrice = userInput > 10 ? userInput * 10 * (1 - 0.05) : userInput * 10
    return totalPrice
}

function totalVacationCost() {
    let questions = {
        car: 'Please enter number of nights you would like to stay in the hotel',
        destination: 'What youre destination?',
        hotel: 'Please, enter of days you would like to rent the car'
    }
    let userInput
    let totalCost = 0, carCost, hotel, planeCost
    for (item in questions) {
        while (true) {
            userInput = prompt(questions[item]);
            validation = item == 'destination' ? isNaN(userInput) : !isNaN(userInput)
            if (userInput != 0 && validation) break;
        }
        switch (item) {
            case 'hotel':
                hotel = hotelCost(userInput)
                totalCost += hotel
                break
            case 'destination':
                planeCost = planeRideCost(userInput)
                totalCost += planeCost
                break
            case 'car':
                carCost = rentalCarCost(userInput)
                totalCost += carCost
                break
        }

    }
    const divVac = document.querySelector('div')
    const myTravel = document.createElement('h1')
    myTravel.innerText = `The car cost: ${carCost}, the hotel cost: ${hotel}, the plane tickets cost: ${planeCost}. Total cost: ${totalCost}`
    divVac.append(myTravel)

}

//totalVacationCost()

console.log('Exercise 5:--------------------------')

const div = document.getElementById('container')
console.log(div)

const newName = document.querySelector('ul').lastElementChild.innerText = 'Richard'

const ulList = document.querySelectorAll('ul')
for (let i = 0; i < 2; i++) {
    ulList[i].firstElementChild.innerText = 'Lidia'
    ulList[i].className = 'student_list'           // <-- for section 3
}

console.log(ulList[0].className)
console.log(ulList[1].className)

ulList[0].classList.add('university', 'attendance')
console.log(ulList[0].className)

div.style.padding = '1vw 5vw'
div.style.backgroundColor = 'lightblue'
ulList[1].lastElementChild.style.display = 'none'
div.nextElementSibling.lastElementChild.style.border = '2px dotted red'
div.nextElementSibling.lastElementChild.style.width = '20vw'
div.parentElement.style.fontSize = '5vw'

const name1 = ulList[0].lastElementChild.innerText
const name2 = ulList[1].firstElementChild.nextElementSibling.innerText
// if (div.style.backgroundColor === 'lightblue') alert(`Hello ${name1} and ${name2}`)

console.log('Exercise 6:--------------------------')

const divNav = document.getElementById('navBar')
divNav.setAttribute('id', 'socialNetworkNavigation')
console.log(divNav.id)

const newLi = document.createElement('li')
newLi.innerHTML = '<a href="#">Logout</a>'
divNav.firstElementChild.appendChild(newLi)

console.log(divNav.firstElementChild.firstElementChild.textContent)
console.log(divNav.firstElementChild.lastElementChild.textContent)

console.log('Exercise 7:--------------------------')

book1 = {
    title: 'It',
    author: 'Stephen King',
    image: 'https://lareviewofbooks-media.azureedge.net/unsafe/1280x0/filters:format(jpeg)/https%3A%2F%2Fdev.lareviewofbooks.org%2Fwp-content%2Fuploads%2F2016%2F09%2Fpaavpdqsbtggtmn4smxs.png',
    alreadyRead: true
}
book2 = {
    title: 'Ubik',
    author: 'Philip K. Dick',
    image: 'https://freight.cargo.site/w/1415/q/75/i/cc82537937a69f9fdbafc1999a3d11673ccef07b3357c94d53b6aa769ddccfc8/Ubik1.jpg',
    alreadyRead: true
}
book3 = {
    title: 'The Man in the High Castle',
    author: 'Philip K. Dick',
    image: 'https://static.wikia.nocookie.net/pkd/images/c/cd/Man-in-the-high-castle-07.jpg',
    alreadyRead: false
}

const allBooks = [book1, book2, book3]
const sectionBook = document.getElementsByClassName('listBooks')[0]

for (book of allBooks) {
    const divBook = document.createElement('div');
    const text = document.createElement('h2');
    text.innerText = `${book.title} written by ${book.author}`
    const image = document.createElement('img');
    image.setAttribute('src', `${book.image}`);
    image.style.width = '100px'
    divBook.appendChild(text);
    divBook.appendChild(image)
    if (book.alreadyRead) divBook.style.color = 'red'
    sectionBook.appendChild(divBook)
}
