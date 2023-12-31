const gameInfo = [
    {
        username: "john",
        team: "red",
        score: 5,
        items: ["ball", "book", "pen"]
    },
    {
        username: "becky",
        team: "blue",
        score: 10,
        items: ["tape", "backpack", "pen"]
    },
    {
        username: "susy",
        team: "red",
        score: 55,
        items: ["ball", "eraser", "pen"]
    },
    {
        username: "tyson",
        team: "green",
        score: 1,
        items: ["book", "pen"]
    },
];

const usernames = [];
gameInfo.forEach((game) => usernames.push(game.username + '!'));
console.log(usernames);

const winners = [];
gameInfo.forEach((game, indx, arr) => game.score > 5 ? winners.push(game.username) : null );
console.log(winners);

const total = gameInfo.reduce((acc, val) => acc + val.score, 0)
console.log(total);
