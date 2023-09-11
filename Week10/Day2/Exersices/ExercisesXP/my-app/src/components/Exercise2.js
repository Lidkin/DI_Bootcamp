import FavoriteAnimals from "./UserFavoriteAnimals";

const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
};

function Exercise2() {
    return <div>
        <h3>{user.firstName}</h3>
        <h3>{user.lastName}</h3>
        <FavoriteAnimals animals={user.favAnimals} />
    </div>
};

export default Exercise2;