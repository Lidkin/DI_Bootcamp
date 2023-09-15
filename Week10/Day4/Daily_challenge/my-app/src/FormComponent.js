
function FormComponent(props) {
    const pronoun = 'Your';
    const styleLi = {
        listStyleType: 'none',
        content: '**',
        marginLeft: '0.5em'
    }

    const { firstname,
        lastname,
        age,
        gender,
        destination,
        nutsFree,
        lactoseFree,
        vegan } = props.inputs;

    return (
        <>
            <h2>Entered Information:</h2>
            <p>{pronoun} name: {firstname} {lastname}</p>
            <p>{pronoun} age: {age}</p>
            <p>{pronoun} gender: {gender}</p>
            <p>{pronoun} destination: {destination}</p>
            <ul>{pronoun} dietary:
                <li style={styleLi}>Nuts free: **{nutsFree ? 'Yes' : 'No'}</li>
                <li style={styleLi}>Lactose free: **{lactoseFree ? 'Yes' : 'No'}</li>
                <li style={styleLi}>Vegan: **{vegan ? 'Yes' : 'No'}</li>
            </ul>
        </>
    )

}

export default FormComponent;