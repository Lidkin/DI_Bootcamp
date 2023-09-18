import './App.css';
import { useState } from 'react';
import quotes from './QuotesDatabase.js';
import QuotesAuthorsBox from './QAbox';


function App() {
  let prevIndex = Math.floor(Math.random() * quotes.length);
  const [quote, setQuote] = useState(quotes[prevIndex]);

  const randomQuote = () => {
    const idx = Math.floor(Math.random() * quotes.length);
    const i = idx === prevIndex ? Math.floor(Math.random() * quotes.length) : idx;
    prevIndex = i;
    return quotes[i];
  }

  const randomColor = () => {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  const handleClick = () => {
    setQuote(randomQuote());    
  }

  return (
    < div className="App">
      <QuotesAuthorsBox
        randomColor={randomColor}
        handleClick={handleClick}
        {...quote}
      />
    </div>
  );
}

export default App;
