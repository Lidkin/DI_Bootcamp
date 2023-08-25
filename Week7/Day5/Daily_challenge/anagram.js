let anagram = (sentence1, sentence2) => sentence1.toLowerCase().replace(/[^a-z]+/g, '').split('').sort().join('') == sentence2.toLowerCase().replace(/[^a-z]+/g, '').split('').sort().join('') ? `"${sentence1}" is an anagram "${sentence2}".` : `"${sentence1}" is not an anagram "${sentence2}".`

console.log(anagram('Astronomer', 'Moon starer'));
console.log(anagram('School master', 'The classroom'));
console.log(anagram('The Morse Code', 'Here come dots'));