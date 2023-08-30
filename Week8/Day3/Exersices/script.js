//Exercise 1, Exercise 3

async function getData() {
    try {
        const response = await fetch('https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My');
        if (!response.ok) {
            throw new Error
        } else {
            console.log(await response.json());
        }
    } catch (error) {
        console.log(error)
    }
}
getData()

//Exercise 2 : Giphy API

async function getSun() {
    const sun = 'sun';
    const offs = 2;
    const lim = 5;

    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/search?q=${sun}&rating=g&offset=${offs}&limit=${lim}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`);
        if (!response.ok) {
            throw new Error
        } else {
            const data = await response.json();
            console.log(data.data);
        }
    } catch (err) {
        console.log(err)
    }
}

getSun()