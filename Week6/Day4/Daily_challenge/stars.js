let star = ''
do {
    star += '* '
    console.log(star)
}
while (star.length < 12)


let stars = ''
for (let i = 1; i < 7; i++) {
    let stars = ''
    for (let j = 0; j < i; j++)
        stars += '* '
    console.log(stars)
}