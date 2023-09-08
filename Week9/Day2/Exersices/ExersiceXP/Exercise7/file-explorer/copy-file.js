const fs = require('fs');

const text = fs.readFileSync('./source.txt', 'utf-8');
console.log(text);
fs.writeFileSync('./destination.txt', text, 'utf-8');