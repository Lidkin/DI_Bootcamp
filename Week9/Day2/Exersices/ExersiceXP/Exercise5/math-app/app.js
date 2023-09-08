const { add, mult } = require('./math.js');
const lodash = require('lodash');

console.log(add(2, 3));
console.log(lodash.add(2, 3));
console.log(mult(5, 6));
console.log(lodash.multiply(5, 6));
