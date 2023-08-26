console.log('--------Exercise 1 : Is_Blank-----------');

const isBlank = (string) => string.length == 0;

console.log(isBlank('')); 
console.log(isBlank('abc')); 

console.log('--------Exercise 2 : Abbrev_name-----------');

const abbrevName = (fullName) => `${fullName.substring(0, fullName.indexOf(' ') + 2)}.`

console.log(abbrevName("Robin Singh")); 

console.log('--------Exercise 3 : SwapCase-----------');

const swapCase = (sentence) => sentence.split('').map(char => char = char.match(/[A-Z]/) ? char.toLowerCase() : char.toUpperCase()).join('');

console.log(swapCase('The Quick Brown Fox'));

console.log('--------Exercise 4 : Omnipresent Value-----------');

const isOmnipresent = (arr, value) => arr.map(arrIn => arrIn.includes(value) === false ? false : true).includes(false) ? false : true; 
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1))
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6))

