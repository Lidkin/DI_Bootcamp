console.log('-----Exercise 1 : Location-----')

const person = {
    nameU: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
};

const { nameU, location: { country, city, coordinates: [lat, lng] } } = person;

console.log(`I am ${nameU} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`); 

console.log('my answer: I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)');

console.log('-----Exercise 2: Display Student Info-----')

function displayStudentInfo(objUser) {
    const { first, last } = objUser;
    console.log(`Your full name is ${first} ${last}.`);
}

displayStudentInfo({ first: 'Elie', last: 'Schoppik' });

console.log('-----Exercise 3: User & Id-----')
const users = { user1: 18273, user2: 92833, user3: 90315 };
console.log(Object.entries(users));

const multUsers = Object.entries(users).map(user => [user[0], user[1] * 2]);

console.log(multUsers);

console.log('-----Exercise 4 : Person Class-----')
class Person {
    constructor(name) {
        this.name = name;
    }
}

const member = new Person('John');
console.log(typeof member);
console.log('my answer: object, typeof operator is not able to distinguish between different classes or their instances')

console.log('-----Exercise 5 : Dog Class-----')

class Dog {
    constructor(nameD) {
        this.nameD = nameD;
    }
};

// 3
class Labrador extends Dog {
    constructor(size) {
        super(nameD);
        this.size = size;
    }
};

console.log('my answer - #3')

console.log('-----Exercise 6 : Challenges-----')

console.log([2] === [2], 
{} === {})

const object1 = { number: 5 };
const object2 = object1;  // same object in memory with object1
const object3 = object2; // same object in memory with object1
const object4 = { number: 5 };

object1.number = 4; // rewrite object1, object2 and object3
console.log(object2.number) //4
console.log(object3.number) //4
console.log(object4.number) //5


//Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin 
class Animal {
    constructor (nameA, typeA, color) {
        this.nameA = nameA;
        this.typeA = typeA;
        this.color = color;
    }
}

class Mamal extends Animal {
    constructor(nameA, typeA, color) {
        super(nameA, typeA, color);
    }
    sound(sound) {
        console.log(`${sound} I'm a ${this.typeA}, named ${this.nameA} and I'm ${this.color}.`)
    }
}

const farmerCow = new Mamal('Lily', 'cow', 'brown and white');
farmerCow.sound('Mooo');