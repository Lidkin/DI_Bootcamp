function compareToTen(num) {
    return new Promise((resolve, reject) => {
        if (num <= 10) {
            resolve(`----- Exercise 1 : Comparison-----:\n${num} < 10`);
        } else {
            reject(`----- Exercise 1 : Comparison-----:\n${num} > 10`);
        }
        
    })
}

compareToTen(15)
    .then(result => console.log(result))
    .catch(error => console.log(error))

compareToTen(8)
    .then(result => console.log(result))
    .catch(error => console.log(error))

new Promise((resolve) => {
    setTimeout(()=>resolve('success'), 4000);
}).then(result => console.log('-----Exercise 2 : Promises-----', result))

Promise.resolve(value = 3).then(result => console.log(' Exercise 3 : Resolve & Reject Instructions', result));

Promise.reject(error='Boo').catch(error => console.log(' Exercise 3 : Resolve & Reject Instructions',
        error));

