console.log('-----------Exercise 1--------------')

const people = ["Greg", "Mary", "Devon", "James"];
console.log(people)

people.splice(people.indexOf('James'), 1, 'Jason')
console.log(people)

people.push('Lidia')
console.log(people)

console.log(people.indexOf('Mary'))

let copyPeople = people.slice(0, 1).concat(people.slice(2, -1))

console.log(copyPeople)

console.log(copyPeople.indexOf('Foo')) // element 'Foo' is not present in the array being searched.

let last = people.pop()
console.log(last)

// Part II - Loops

console.log('--People:')
people.forEach(person => { 
        console.log(person)
    }
)

console.log('--before Devon: ')
for (let person of people) {
    if (person != 'Devon') { console.log(person) }
    else { break; }
}

console.log('-------Exercise 2 : Your Favorite Colors------')
let colors = ['red', 'black', 'blue', 'green', 'yellow']

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i+1}st choice is ${colors[i]}`)
}

console.log('----------Exercise 3 : Repeat The Question----------')

let number = prompt('Give me a number')
if (typeof (number).isNaN === true) {
    alert('Shoold to be a number!')
} else { 
    while (number < 10) { 
       number = prompt('Give me a new number')
    }
    alert(`Youre number: ${number}`)
}

console.log('---------Exercise 4 : Building Management---------------')

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor)
console.log(building.nameOfTenants[1])

let sumRent = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]
let danRent = building.numberOfRoomsAndRent.dan[1]
danRent = sumRent > danRent ? 1200 : danRent
console.log(danRent)

console.log('--------------Exercise 5 : Family------------')

let family = {
    lastName: 'Stark',
    members: ['Garry', 'Mary', 'Dov'],
    pets: {
        cats: ['Snowball', 'Blacky'],
        dogs: 'Rex'
    }
}

for (key in family) { 
    console.log(key)
}

for (key in family) { 
    console.log(family[key])
}

console.log('--------------Exercise 6 : Rudolf -----------------')

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}

let string = ''
for (det in details) { 
    string += `${det} ${details[det]} `
}
console.log(string)

console.log('--------------Exercise 7 : Secret Group -----------------')

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let nameSociety = ''
for (n of names.sort()) {
    nameSociety += `${n[0]}`
}
console.log(nameSociety) 