let currentUser;
const repeatDiv = document.createElement('div');
const exitDiv = document.createElement("div");
const allScore = document.createElement("div");

const userAuthorization = (event) => {
    event.preventDefault();
    const userNameInput = document.createElement('form');
    userNameInput.innerHTML = `<fieldset><legend for="userInput">Please input here your name:</legend>
    <input type="text" id="userInput"/></fieldset>`;
    startGame.replaceWith(userNameInput);
    userNameInput.addEventListener('submit', newUser);
}

const newUser = async (event) => {

    try {
        event.preventDefault();
        const body = { userName: event.target.userInput.value, score: 0 };
        const options = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body),
            cache: 'no-cache'
        };
        const res = await fetch('http://localhost:3002/api/users', options);
        if (res.ok) {
            const data = await res.json();
            const userData = data;
            currentUser = userData;
            gameField(userData, event);
        };
    } catch (error) {
        console.log(error);
    };

};

const gameField = (user, event) => {
    const welcome = document.createElement('h1');
    welcome.textContent = `Welcome, ${user.userName}!`;
    event.target.replaceWith(welcome);
    getRandomEmoji();
};

const getRandomEmoji = async () => {
    try {
        const res = await fetch('http://localhost:3002/api/emojis')
        if (res.ok) {
            const data = await res.json();
            gameForm(data);
        } else {
            throw new Error;
        };
    } catch (error) {
        console.log(error);
    };
};

const gameForm = (data) => {
    const emojiData = data.randomEmoji;
    if (emojiImage.hasChildNodes()) {
        emojiImage.removeChild(emojiImage.firstElementChild);
        message.innerText = "";
        scoreuser.replaceChildren();
    }
    const emoji = document.createElement('p');
    emoji.innerText = emojiData.emoji;
    emojiImage.appendChild(emoji);
    game(emojiData);
};

const game = (data) => {
    const answer = data.answer;
    form.innerHTML = `<fieldset>
            <legend>Please select your answer:</legend>
            <div id="input"></div>
            <div><button id="confirm" onclick="gameResult('${answer}')">Confirm</button></div>
            </fieldset>`;
    data.name.forEach((name, index) => {
        const div = document.createElement('div');
        div.innerHTML = `<input type="radio" id="option${index}" name="answer" value="${name}" /><label for="option${index}">${name}</label>`;
        input.appendChild(div);
    });
};

const gameResult = async (answer) => {
    try {
        const confButton = document.querySelector('#confirm');
        let message;
        const selectedAnswer = document.querySelector("input[name=answer]:checked")?.value;
        if (selectedAnswer) {
            confButton.disabled = true;
            if (answer == selectedAnswer) {
                message = 'Greate Job!';
                putResult();
            } else {
                message = 'Sorry, but no...';
            }
            const result = document.querySelector("#message");
            result.textContent = message;
            buttons();
        } else {
            alert('Please select an answer before confirming.');
        };
    } catch (error) {
        console.log(error);
    };
};

const putResult = async () => {
    const user = currentUser;
    try {
        const userBody = await getUser(user.id);
        const options = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userBody),
            cache: 'no-cache'
        };
        const resPut = await fetch("http://localhost:3002/api/users", options);
        if (resPut.ok) {
            const data = await resPut.json();
            const p = document.createElement('p');
            p.innerText = `Your score: ${data.score}.`;
            scoreuser.appendChild(p);
            allScore.innerHTML = `<button>Score of everybody</button>`;
            scoreuser.appendChild(allScore);
            allScore.addEventListener('click', usersScore);
        } else {
            throw new Error;
        };
    } catch (error) {
        console.log(error);
    };
};

const getUser = async (id) => {
    const resGet = await fetch(`http://localhost:3002/api/users/${id}`);
    if (resGet.ok) {
        const { id, userName, score } = await resGet.json();
        const update = { id, userName, score: score + 1 };
        return update;
    } else {
        throw new Error;
    };
};

const buttons = () => {
    repeatDiv.innerHTML = `<button onclick="getRandomEmoji()">One more time?</button>`;
    scoreuser.appendChild(repeatDiv);
    exitDiv.innerHTML = "<button onclick='window.location.reload()'>Exit</button>";
    scoreuser.appendChild(exitDiv);
};

const usersScore = async () => {
    try {
        let data;
        const res = await fetch("http://localhost:3002/api/score");
        if (res.ok) {
            data = await res.json();
        }
        const scoreList = data.map(item => `${item.userName} - ${item.score}`);
        const p = document.createElement('p');
        p.innerText = "Gamers: \n" + scoreList.join('\n');
        allScore.replaceWith(p);
    } catch (error) {
        console.log(error);
    };
};