const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

stringNum = numbers.toString()
stringNumJoin = numbers.join(' ')

console.log(stringNum, '\n', stringNumJoin)

//----------Bonus------------

console.log(numbers)
let max
while (true) {
    let swap = 0
    for (let i = 0; i < numbers.length - 1; i++) {
        if (numbers[i] < numbers[i + 1]) {
            max = numbers[i + 1]
            numbers[i + 1] = numbers[i]
            numbers[i] = max
            swap++
        }
    }
    if (swap == 0) { break }
}

console.log(numbers)
