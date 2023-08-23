// Exercise 1:

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

colors.forEach((color, indx) => {
    console.log(`${indx + 1}# choice is ${color}`);
});

colors.some((color) => color === 'Violet' ? console.log('Yeah') : console.log('No...'));

// Exercise 2:

const ordinal = ["th", "st", "nd", "rd"];

colors.forEach((color, indx) => {
    console.log(`${indx + 1}${indx < 3 ? ordinal[indx + 1] : ordinal[0]} choice is ${color}`);
});

// Exercise 3:

console.log('-----1-----', ['bread', "carrot", "potato", 'chicken', "apple", "orange"]);

console.log('-----2-----', ['U','S','A']);

console.log('-----Bonus-----', [, ,], 'correctAnswer: [ undefined, undefined ]');

// Exercise 4:
const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
{ firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
{ firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
{ firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
{ firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
{ firstName: 'Wes', lastName: 'Reid', role: 'Instructor' },
    { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor' }];

const greting = users.map((user) => `Hello ${user.firstName}`);
console.log(greting);

const fullStacks = users.filter(user => user.role === 'Full Stack Resident');
console.log(fullStacks);

const onlyLastName = users.filter(user => user.role === 'Full Stack Resident').map((user) => user.lastName);
console.log(onlyLastName);

// Exercise 5:
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
const sentence = epic.reduce((acc, val) => `${acc} ${val}`);
console.log(sentence);

// Exercise 6:

const students = [{ name: "Ray", course: "Computer Science", isPassed: true },
{ name: "Liam", course: "Computer Science", isPassed: false },
{ name: "Jenner", course: "Information Technology", isPassed: true },
{ name: "Marco", course: "Robotics", isPassed: true },
{ name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
    { name: "Jamie", course: "Big Data", isPassed: false }];

const passed = students.filter(student => student.isPassed).forEach((student) => console.log(`Good job ${student.name}, you passed the course in ${student.course}!`));
console.log(passed);