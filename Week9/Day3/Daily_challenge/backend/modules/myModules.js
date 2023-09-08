const fs = require('fs');
const { emojis } = require('../config/db.js');

const getRandomEmoji = () => {
    const index = () => Math.floor(Math.random() * emojis.length);
    const indEm = index();
    const { emoji, name } = emojis[indEm];
    let arrNames = [];
    arrNames.push(name);
    for (let i = 1; i < 4; i++){
        let ind = index();
        while (indEm == ind) {
            ind = index();
            if (arrNames.some(name => name == emojis[ind])) ind = index();
        }
        arrNames.push(emojis[ind].name);
    }
    const names = shuffleNames(arrNames);
    return { emoji:emoji, name: names , answer: name};
};

const shuffleNames = (arr) => {
    const newArr = [...arr];
    for (let i = newArr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [newArr[i], newArr[j]] = [newArr[j], newArr[i]];
    }
    return newArr;
};

const randomEmoji = getRandomEmoji();

function saveDataToFile(data, filePath) {
    fs.writeFile(filePath, JSON.stringify(data, null, 2), (err) => {
        if (err) {
            console.error('Error writing to file:', err);
        } else {
            console.log(`Data has been saved to ${filePath}`);
        }
    });
};

let usersDb;

try {
    const data = fs.readFileSync('./config/users.json', 'utf8');
    usersDb = JSON.parse(data);
} catch (error) {
    console.error('Error reading or parsing file:', error);
}

module.exports = { randomEmoji, saveDataToFile, usersDb };