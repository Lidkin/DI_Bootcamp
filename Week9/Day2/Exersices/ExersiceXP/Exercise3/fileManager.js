import fs from 'fs';

export const readFile = (file) => fs.readFileSync(file, 'utf-8', (err) => { if (err) return console.log(err) });
export const writeFile = (file, content) => fs.writeFileSync(file, JSON.stringify(content), (err) => { if (err) return console.log(err) });