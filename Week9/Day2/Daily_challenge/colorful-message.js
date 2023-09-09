import chalk from 'chalk';

const colorful = (text) => {
    if (text.length % 2 == 0) {
        return chalk.bgRed(text);
    } else {
        return chalk.greenBright(text);
    }
};

export default colorful;