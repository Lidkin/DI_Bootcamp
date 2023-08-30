//`https://api.giphy.com/v1/gifs/search?q=${event.target.gif.value}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`
const images = document.createElement('div');
container.appendChild(images);

async function gifs(event) {
    event.preventDefault();
    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${event.target.gif.value}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
        if (response.ok) {
            const data = await response.json();
            //const gif = data.data[`${Math.round(Math.random() * data.data.length)}`].images.original.url;
            const gif = data.data.images.original.url;
            createImage(gif);
            if (images.childElementCount <= 1) createButDelAll();
        } else {
            throw new Error
        }
    } catch (err) {
        console.log(err)
    }
}

formRand.addEventListener('submit', gifs);

function createImage(gif) {
    const section = document.createElement('section');
    images.appendChild(section);
    const imageGif = document.createElement('img');
    imageGif.setAttribute('src', gif);
    imageGif.style.width = '500px';
    section.appendChild(imageGif);
    const buttonDel = document.createElement('button');
    buttonDel.innerText = 'DELETE';
    section.appendChild(buttonDel);
    deleteGif(buttonDel, section);
};

function deleteGif(buttonDel, section) {
    buttonDel.addEventListener('click', () => {
        section.remove();
    })
};

function createButDelAll() {
    const deleteAllBut = document.createElement('button');
    deleteAllBut.innerText = 'DELETE ALL';
    deleteAllBut.setAttribute('id', 'deleteAll');
    container.appendChild(deleteAllBut);
    deleteAll(deleteAllBut);
};

function deleteAll(deleteAllBut) {
    deleteAllBut.addEventListener('click', () => {
        images.remove();
        deleteAllBut.remove();
        window.top.location.reload();
    });
};

