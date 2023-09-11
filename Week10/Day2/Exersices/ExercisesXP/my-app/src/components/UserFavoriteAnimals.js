function FavoriteAnimals(props) {
    const { animals } = props;
    return <ul>{animals.map((item, index) => { return <li key={index}>{ item}</li>} )}</ul>
}

export default FavoriteAnimals;