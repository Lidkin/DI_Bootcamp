const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, '..', '/config', 'users.json');

const usersDB = async () => {
    try {
        const data = await fs.promises.readFile(filePath, 'utf8');
        return JSON.parse(data);
    } catch (err) {
        console.error('Error reading JSON file:', err);
    }
}

const usersToDB = async (newData) => {
    try {
        await fs.promises.writeFile(filePath, JSON.stringify(newData, null, 2));
    } catch (err) {
        console.error('Error writing JSON file:', err);
    }
};

module.exports = { usersDB, usersToDB };