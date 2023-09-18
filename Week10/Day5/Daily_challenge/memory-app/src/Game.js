import { useState } from 'react';
import superheroes from './superheroes.json';

const Game = (props) => {
    const [cards, setCards] = useState(superheroes.superheroes);
    const [score, setScore] = useState(0);
    const [maxscore, setMaxscore] = useState(0);

    const clickCard = (e) => {
        let arr;
        const id = e.target.parentElement.id;
        const index = cards.findIndex(card => card.id == id);
        const clikedCard = getScore(index);
        if (clikedCard.clicked) {
            cards.splice(index, 1, clikedCard);
            arr = shuffleCards(cards);
        }
        else {
            arr = cards.map(card => { return ({ ...card, clicked: false }) });
        }
        setCards([...arr]);
    };

    const getScore = (index) => {
        const newScore = score + 1;
        setMaxscore(maxscore < newScore ? newScore : maxscore);
        const wasClicked = cards[index];
        if (wasClicked.clicked) {
            setScore(0);
            setMaxscore(maxscore);
            wasClicked.clicked = false;
        } else {
            setScore(newScore);
            wasClicked.clicked = true;
        }
        return wasClicked;
    }

    const shuffleCards = (arr) => {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    };

    return (
        <>
            <header>
                <h2>Superheroes Memory Game</h2>
                <p>Score: {score}  Top Score: {maxscore}</p>
            </header>
            <article>Get points by clicking on an image but don't click on any more than once!</article>
            <div className='grid-container'>
                {cards.map((card) => {
                    return (
                        <div className='card' id={card.id} key={card.id} >
                            <img onClick={(e) => clickCard(e)} src={card.image} />
                            <p><span>Name: </span>{card.name}</p>
                            <p><span>Occupation: </span>{card.occupation}</p>
                        </div>)
                })}
            </div>
        </>
    )
};


export default Game;