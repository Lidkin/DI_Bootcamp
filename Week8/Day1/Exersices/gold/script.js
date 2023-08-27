console.log('-------Exercise 1 : Print Full Name-------')

const printFullName = (nameObj) => console.log('Your full name is ' + Object.values(nameObj).join(' '));

const printFullNameD = ({ first, last }) => console.log(`Your full name is ${first} ${last}`);
    
printFullName({ first: 'Elie', last: 'Schoppik' });
printFullNameD({ first: 'Elie', last: 'Schoppik' });

console.log('-------Exercise 2 : Keys And Values-------')

const keysAndValues = (obj) => console.log([Object.keys(obj), Object.values(obj)]);
keysAndValues({ a: 1, b: 2, c: 3 });
keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" });
keysAndValues({ key1: true, key2: false, key3: undefined });

console.log('-------Exercise 3 : Counter Class------- ')

class Counter {
    constructor() {
        this.count = 0;
    }

    increment() {
        this.count++;
    }
}

const counterOne = new Counter();
counterOne.increment();
counterOne.increment();

const counterTwo = counterOne;
counterTwo.increment();
console.log(counterOne === counterTwo)


console.log('my answer 2, but is 3, becouse counterOne === counterTwo is true and increment called 3th time')
console.log(counterOne.count);
