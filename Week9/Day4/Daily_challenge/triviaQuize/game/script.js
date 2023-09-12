let quizList;

const waitForEnterKey = async (element) => {
    return new Promise((resolve) => {
        const handleKeyDown = (event) => {
            if (event.key === 'Enter') {
                element.removeEventListener('keydown', handleKeyDown);
                resolve();
            }
        };
        element.addEventListener('keydown', handleKeyDown);
    });
};

const startGame = async () => {
    try {
        quizList = await quiz();
        console.log(quizList)
        if (!quizList) throw new Error();

        for (const question of quizList) {
            const game = document.createElement('div');
            game.innerHTML = `<p>${question}</p>
                <input type='text' placeholder='Your Answer'></input>
                <p id='msg'></p>
                <br>`;
            quizGame.appendChild(game);

            const answerInput = game.querySelector('input');
            await waitForEnterKey(answerInput);

            const answer = answerInput.value;
            const message = await postAnswer(question, answer);
            const msg = game.querySelector('#msg');
            msg.innerText = message;
        }

        const scoreGame = await scores();
        const score = document.querySelector('#score');
        score.innerText = `Your score: ${scoreGame}`;
    } catch (err) {
        console.log(err);
    }
};

const quiz = async () => {
    try {
        const res = await fetch('http://localhost:3000/quiz');
        if (res.ok) {
            const data = await res.json();
            return data;
        } else {
            throw new Error;
        }
    } catch (error) {
        console.log(error);
    };
};

const postAnswer = async (question, answer) => {
        try {
            const body = { question, answer };
            const options = {
                method: 'POST',
                body: JSON.stringify(body),
                headers: {
                    "Content-Type": "application/json"
                },
            };
            const res = await fetch('http://localhost:3000/quiz', options);
            if (res.ok) {
                const data = await res.json();
                return data.msg;
            } else {
                throw new Error;
            }
        } catch (error) {
            console.log(error);
        }
};

const scores = async () => {
    try {
        const res = await fetch('http://localhost:3000/quiz/score');
        if (res.ok) {
            const data = await res.json();
            console.log(data)
            return data.score;
        } else {
            throw new Error;
        }
    } catch (error) {
        console.log(error);
    }
};