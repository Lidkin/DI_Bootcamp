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


// Bonus: To do this Bonus look up how to work with nested for loops
// Sort the numbers array in descending order, do so using for loops(Not using built -in sort methods).
// The output should be: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
// Hint: The algorithm is called “Bubble Sort”
// Use a temporary variable to swap values in the array.
    // Use 2 “nested” for loops(Nested means one inside the other).
// Add comments and console.log the result for each step, this will help you understand.
    // Requirement: Don’t copy paste solutions from Google