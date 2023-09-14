import './App.css';
import React from 'react';
import ErrorBoundary from './ErrorBoundary.js';

class BuggyCounter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { counter: 0 };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState({ counter: this.state.counter + 1 });
  }

  render() {
    if (this.state.counter > 5) throw new Error("I crashed!");
    return (
      <>
        <h1 onClick={this.handleClick}> Score {this.state.counter}</h1>
      </>
    )

  }

}

function App() {
  return (
    <div>
      <ErrorBoundary>
        <BuggyCounter />
        <BuggyCounter />
      </ErrorBoundary>
      <hr />
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <hr />
      <BuggyCounter />
    </div>
  )
}

export default App;
