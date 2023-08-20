const planet1 = {
    nameP: 'Mercury',
    color: 'salmon',
    moon: null
}

const planet2 = {
    nameP: 'Venus',
    color: 'pink',
    moon: null
}

const planet3 = {
    nameP: 'Earth',
    color: 'lightblue',
    moon: ['Moon']
}

const planet4 = {
    nameP: 'Mars',
    color: 'red',
    moon: ['Phobos', 'Deimos']
}

const planet5 = {
    nameP: 'Jupiter',
    color: 'lightgray',
    moon: ['Io', 'Europa', 'Ganymede', 'Callisto']
}

const planet6 = {
    nameP: 'Saturn',
    color: 'gold',
    moon: ['Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan', 'Hyperion', 'Iapetus', 'Phoebe', 'Janus', 'Epimetheus', 'Helene', 'Telesto', 'Calypso', 'Atlas', 'Prometheus', 'Pandora', 'Pan', 'Ymir', 'Paaliaq', 'Tarvos', 'Ijiraq', 'Suttungr', 'Kiviuq', 'Mundilfari', 'Albiorix', 'Skathi']
}

const planet7 = {
    nameP: 'Uranus',
    color: 'orange',
    moon: ['Ariel', 'Belinda', 'Bianca', 'Caliban', 'Cordelia', 'Cressida', 'Cupid', 'Desdemona', 'Ferdinand', 'Francisco', 'Juliet', 'Mab', 'Margaret', 'Miranda', 'Oberon', 'Ophelia', 'Perdita', 'Portia', 'Prospero', 'Puck', 'Rosalind', 'Setebos', 'Stephano', 'Sycorax', 'Titania', 'Trinculo', 'Umbriel']
}
const planet8 = {
    nameP: 'Neptune',
    color: 'blue',
    moon: ['Despina', 'Galatea', 'Halimede', 'Hippocamp', 'Laomedeia', 'Larissa', 'Naiad', 'Nereid', 'Neso', 'Proteus', 'Psamathe', 'Sao', 'Thalassa', 'Triton']
}
const planet9 = {
    nameP: 'Pluto',
    color: 'gray',
    moon: ['Charon', 'Hydra', 'Kerberos', 'Nix', 'Styx']
}

allPlanets = [planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8, planet9]

const section = document.getElementsByClassName('listPlanets')[0]

for (plan of allPlanets) {
    let div = document.createElement('div')
    div.classList.add('planet', `${plan.nameP}`)
    div.style.backgroundColor = `${plan.color}`
    div.innerText = `${plan.nameP}`
    div.style.margin = '20px 20px'

    if (plan.moon != null) {
        let left = 10;
        let top =15;
        for (m of plan.moon) {
            let divMoon = document.createElement('div');
            divMoon.className = 'moon';
            divMoon.innerText = `${m}`;
            divMoon.style.left = `${left}px`
            divMoon.style.top = `${top}px`;
            divMoon.style.fontSize = '10px'
            divMoon.style.display = 'flex';
            divMoon.style.justifyContent = 'center';
            divMoon.style.alignItems = 'center';
            divMoon.style.margin = '20px 20px'
            div.appendChild(divMoon)
            left += 40
            if (left > 600) {
                top += 40;
                left = 10;
            } 
        }
    }
    div.style.alignItems = 
    section.appendChild(div)
}