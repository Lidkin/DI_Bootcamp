const express = require('express');
const router = express.Router();

let score = 0;

const triviaQuestions = [
    {
        question: "What is the capital of France?",
        answer: "Paris",
    },
    {
        question: "Which planet is known as the Red Planet?",
        answer: "Mars",
    },
    {
        question: "What is the largest mammal in the world?",
        answer: "Blue whale",
    },
]; 

router.get('/quiz', (req, res) => {
    res.status(200).json(triviaQuestions.map(item => item.question));
});

router.post('/quiz', (req, res) => {    
    const { question, answer } = req.body;
    const idx = triviaQuestions.findIndex(item => item.question == question);
    if (triviaQuestions[idx].answer != answer) return res.status(200).json({ msg: "Wrong Answer!" });
    score += 1;
    res.status(200).json({ msg: 'Great Job!' });
});
 
router.get('/quiz/score', (req, res) => {
    res.status(200).json({ score });
});

module.exports = router;
