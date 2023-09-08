const { products } = require('./products.js');


const findProduct = (nameP) => products.find((product) => product.name === nameP);

console.log(findProduct('tea'));
console.log(findProduct('croissant'));
console.log(findProduct('beer'));