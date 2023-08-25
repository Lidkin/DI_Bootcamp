import robots from './robots.js';

function navBar() {
    let navBar = document.querySelector('nav');
    let label = document.createElement('label');
    let input = document.createElement('input');

    label.setAttribute('for', 'search');
    label.setAttribute('id', 'label');
    input.setAttribute('id', 'search');
    input.setAttribute('type', 'search');
    input.setAttribute('placeholder', 'Search Robots')
    label.innerText = 'robofriends'.toUpperCase();

    navBar.appendChild(label);
    navBar.appendChild(input);
    showRobots(robots);
    inputListener(input)
}

function inputListener(input) {
    input.addEventListener('keyup', (event) => {
        showRobots();
        event.preventDefault();
        let letters = event.target.value.toLowerCase();
        let foundRobots = robots.filter(robot => robot.name.toLowerCase().startsWith(letters, 0) || robot.email.toLowerCase().startsWith(letters, 0));
        if (foundRobots.length == 0) {
            input.value = "Robot-friend not found :`(";
            showRobots([{ image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPeopN09hE3ZwvuvRyYk4K6CXbkkkDyxMgkQ&usqp=CAU' }]);
            input.addEventListener('click', () => location.reload());
        } else {
            showRobots(foundRobots);
        };
    });
}

function showRobots(robots_arr = []) {
    const Cards = document.querySelector('.row');

    if (robots_arr.length != 0) {
        robots_arr.forEach((robot) => {
            createCard(Cards, robot);
        });
    } else {
        Cards.replaceChildren('');
    }
};

function createCard(Cards, robot) {
    const Div = document.createElement('div');
    const CardDiv = document.createElement('div');
    Div.setAttribute('class', 'col');
    CardDiv.setAttribute('class', 'card h-100');
    Cards.appendChild(Div);
    Div.appendChild(CardDiv);
    CardDiv.appendChild(image(robot)[0]);
    CardDiv.appendChild(image(robot)[1]);
}

function image(robot) {
    let image = document.createElement('img');
    image.setAttribute('src', robot.image);
    image.setAttribute('class', 'card-img-top rounded-circle');
    let about = document.createElement('p');
    about.innerText = robot.name ? `${robot.name}
       ${robot.email}` : 'Poor Lonely Robot';
    return [image, about];    
}

navBar();