import chalk from 'chalk';

const name = 'Sindre';
console.log(chalk.green('Hello %s'), chalk.bgCyan(chalk.bold(name)));

const text = 'Lucky day!';
const arr = text.split(' ');
const el1 = chalk.red.italic(arr[0]);
const el2 = chalk.yellow.bold(arr[1]);
const chalkArr = [el1, el2];
const newStr = chalkArr.join(' ');
console.log(newStr);
console.log(chalk.bgGreen(newStr));

