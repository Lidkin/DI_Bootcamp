function replaceIn(sentence) {
    let wordNot = sentence.indexOf('not')
    let wordBad = sentence.indexOf('bad')

    if (wordBad > wordNot && wordNot != -1) {
        sentence = sentence.replace(sentence.substring(wordNot, wordBad + 3), 'good')
    }
    return sentence
}

console.log(replaceIn('This dinner is not that bad! You cook well'))
console.log(replaceIn('This movie is not so bad.'))
console.log(replaceIn('This weather is so bad!'))