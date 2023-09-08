const fs = require('fs');

const listFiles = fs.readdirSync('./');
console.log(listFiles);