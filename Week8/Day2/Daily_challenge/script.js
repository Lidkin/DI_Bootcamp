function makeAllCaps(words) {
    return new Promise((resolve, reject) => {
        if (words.every((element) => typeof element === 'string')) {
            resolve(words.map(word => word.toUpperCase()));
        } else {
            reject("It's array didn't have any strings.");
        }
    })
}

function sortWords(wordsUp) {
    return new Promise((resolve, reject) => {
        if (wordsUp.length > 4) {
            resolve(wordsUp.sort())
        } else {
            reject("It's array to short.")
        }
    })
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
    .catch(error => console.log(error));

console.log('---2nd Daily Challenge---')
var start = performance.now();

const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`

function toJs(morse) {
    return new Promise((resolve, reject) => {
        if (morse.length != 0) {
            resolve(JSON.parse(morse))
        } else {
            reject('error')
        }
    });
}

function toMorse(morseJS) {
    let userImput = prompt('Enter some word or sentence:').trim();
    const arrUserInput = userImput.replace(/\s/g, '').toLowerCase().split('');
    const jsonKey = Object.keys(morseJS);
    const isValidChar = arrUserInput.every(char => jsonKey.includes(char));
    return new Promise((resolve, reject) => {
        if (isValidChar) {
            resolve([arrUserInput.map(char => morseJS[char]), userImput]);
        } else {
            reject(` doesn't exist in the morse javascript object`);
        }
    });
};

function joinWords(morseTranslation) {
    console.log(morseTranslation)
    const body = document.querySelector('body');
    const result = document.createElement('h1');
    result.innerText = `${morseTranslation[1]} \n` + morseTranslation[0].join('\n');
    result.style.textAlign = 'center';
    body.appendChild(result);
}

toJs(morse)
    .then((morseJS) => toMorse(morseJS))
    .then((morseTranslation) => joinWords(morseTranslation))
    .catch(error => console.log(error));

var duration = performance.now() - start;

console.log('duration', duration)