let randomNum = Math.round(Math.random() * 83);
let previousNum;
async function starWars() {
    if (previousNum === randomNum) { randomNum = Math.round(Math.random() * 83); }
    
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${randomNum}`);
        if (response.ok) {
            const character = await response.json();
            aboutCharacter(character.result.properties);
            previousNum = randomNum;
        } else {
            throw new Error;
        }
    } catch {
        info.innerHTML = "<p style='margin-top: 70px;'>Oh No! That person isn't available.</p>"
    }
};

document.querySelector('button').addEventListener('click', starWars);

async function aboutCharacter(character) {
    info.innerText = '';
    info.classList.add("fa-3x");
    const i = document.createElement('i');
    i.className = "fa-solid fa-sync fa-spin";
    info.appendChild(i);
    const world = character['homeworld'];
    const NameWorld = await nameWorld(world);

    info.innerHTML = `<p>${character['name']}</p><br>
    <p class='p'>${character['height']}</p><br>
    <p class='p'>${character['gender']}</p><br>
    <p class='p'>${character['birth_year']}</p><br>
    <p class='p'>${NameWorld.result.properties['name']}</p><br>
    `
}

async function nameWorld(world) {
    if (world !== 'unknown') {
        const worldName = await fetch(world);
        const data = await worldName.json()
        return data;
    }
} 