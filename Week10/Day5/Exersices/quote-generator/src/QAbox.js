function QuotesAuthorsBox(props) {
    
    const color = props.randomColor();
    document.querySelector('body').style.backgroundColor = color;

    return (
        <div className="box">
            <header>{props.quote}</header>
            <h5>-{props.author}-</h5>
            <button onClick={() => { props.handleClick() }} id="newquote" style={{ backgroundColor: color }} >New Quote</button>
        </div>
    )
}
 
export default QuotesAuthorsBox;