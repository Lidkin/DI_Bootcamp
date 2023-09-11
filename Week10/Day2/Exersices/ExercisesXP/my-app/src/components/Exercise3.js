const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
};

function Exercise() {
    const link = 'https://www.lidiakhait.com/';
    const myimage = 'https://images.unsplash.com/photo-1603984973710-e915353b35fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YW1hemluZyUyMHBpY3R1cmV8ZW58MHx8MHx8fDA%3D&w=1000&q=80'
    const list = ['Install', 'Init', 'Delete'];
    return <div style={{ textAlign: 'center', padding: '2px' }}>
        <h1 style={style_header}>This is a Header</h1>
        <p className='para'>This is Paragraph</p>
        <a href={{link}}>My Page</a>
        <form style={{margin:'2px'}}>
            <label htmlFor="fname">Name:</label>
            <input type="text" id="fname" name="fname"/>
        </form>
        <img src={ myimage } style={{width: '200px'}} alt="spring"></img>
        <ul style={{ listStylePosition: 'inside' }}>About coding:{list.map(item => { return <li>{item }</li> })}</ul>
    </div>
}

export default Exercise;