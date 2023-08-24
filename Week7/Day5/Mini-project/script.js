const robots = [
    {
        id: 1,
        name: 'Leanne Graham',
        username: 'Bret',
        email: 'Sincere@april.biz',
        image: 'https://robohash.org/1?200x200'
    },
    {
        id: 2,
        name: 'Ervin Howell',
        username: 'Antonette',
        email: 'Shanna@melissa.tv',
        image: 'https://robohash.org/2?200x200'
    },
    {
        id: 3,
        name: 'Clementine Bauch',
        username: 'Samantha',
        email: 'Nathan@yesenia.net',
        image: 'https://robohash.org/3?200x200'
    },
    {
        id: 4,
        name: 'Patricia Lebsack',
        username: 'Karianne',
        email: 'Julianne.OConner@kory.org',
        image: 'https://robohash.org/4?200x200'
    },
    {
        id: 5,
        name: 'Chelsey Dietrich',
        username: 'Kamren',
        email: 'Lucio_Hettinger@annie.ca',
        image: 'https://robohash.org/5?200x200'
    },
    {
        id: 6,
        name: 'Mrs. Dennis Schulist',
        username: 'Leopoldo_Corkery',
        email: 'Karley_Dach@jasper.info',
        image: 'https://robohash.org/6?200x200'
    },
    {
        id: 7,
        name: 'Kurtis Weissnat',
        username: 'Elwyn.Skiles',
        email: 'Telly.Hoeger@billy.biz',
        image: 'https://robohash.org/7?200x200'
    },
    {
        id: 8,
        name: 'Nicholas Runolfsdottir V',
        username: 'Maxime_Nienow',
        email: 'Sherwood@rosamond.me',
        image: 'https://robohash.org/8?200x200'
    },
    {
        id: 9,
        name: 'Glenna Reichert',
        username: 'Delphine',
        email: 'Chaim_McDermott@dana.io',
        image: 'https://robohash.org/9?200x200'
    },
    {
        id: 10,
        name: 'Clementina DuBuque',
        username: 'Moriah.Stanton',
        email: 'Rey.Padberg@karina.biz',
        image: 'https://robohash.org/10?200x200'
    }
];

function navBar() {
    let navBar = document.querySelector('nav');
    let label = document.createElement('label');
    let input = document.createElement('input');

    label.setAttribute('for', 'search');
    label.setAttribute('id', 'label');
    input.setAttribute('id', 'search');
    input.setAttribute('type', 'search');
    input.setAttribute('placeholder', 'Search Robots')
    label.innerText = 'robofriends'

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
    let image = document.createElement('img');
    image.setAttribute('src', robot.image);
    image.setAttribute('class', 'card-img-top');
    let about = document.createElement('p');
    about.innerText = robot.name ? `${robot.name}
       ${robot.email}` : 'Poor Lonely Robot';
    CardDiv.appendChild(image);
    CardDiv.appendChild(about);
}

navBar();