import fs from 'fs';
const path = 'C:/Users/lidia/Documents/Programming/DI_course/DI_bootcamp/Week9/Day2/Daily_challenge/files/file-data.txt';

const text = fs.readFileSync(path, 'utf-8');

export default text;