const rand = () => {
    let random = 0;
    while (random < 0.9) {
        random = Math.random();
    };
    return random
 };
const fillBooks = () => {
    let books = [];
    for (let i = 1; i < 11; i++) {
        books.push({ id: i, title: `title${i}`, author: `author${i}`, publishedYear: Math.floor(rand() * 2020) });
    };
    return books;
}

const booksDB = fillBooks();
const books = [...booksDB];

module.exports = books;