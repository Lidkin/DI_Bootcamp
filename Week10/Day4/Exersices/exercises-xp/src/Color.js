import React from "react";

class Color extends React.Component {
    constructor(props){
        super(props);
        this.state = { color: 'red', show: true }
    }  

    shouldComponentUpdate(prevProps, prevState) {
        if (prevState.color !== this.state.color) {
            return true;
        }
        else {
            this.setState({ color: "red" })
            return false;
        }
    }
    
    componentDidMount() {
        setTimeout(() => {
            this.setState({ color: 'yellow' });
        }, 2000);
    }

    getSnapshotBeforeUpdate(prevProps, prevState) {
        console.log("in getSnapshotBeforeUpdate, prevState color:", prevState.color);
        return prevState.color;
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        console.log("after update, color before update:", snapshot);
    }

    
    render() { 
        return (
            <>
                <h1>My Favorite Color is <i>{this.state.color}</i></h1>
                <button onClick={() => this.setState({ color: "blue" })}>Change Color</button>
                <Child show={this.state} />
            </>
        )
    }
}

class Child extends React.Component {
    constructor(show) {
        super();
        this.state = {show}
}
    componentWillUnmount() { 
        if (this.state.show) alert("Unmounted message")
    }

    render() { 
        if (this.state.show) {
            return (
                <header>Hello World!<button onClick={() => { this.setState({ show: false }) }}>Delete Header</button></header>
            )
        }       
    }
}
export default Color;