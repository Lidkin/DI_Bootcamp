import { writeFile, readFile } from "./fileManager.js";

const reading = readFile('./Hello Word.txt');
console.log(reading);

writeFile('./Bye World.txt', 'Writing to the file');