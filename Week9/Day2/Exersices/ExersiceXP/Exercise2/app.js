import userData from './data.js';

const averageAge = () => { const average = userData.reduce((age, nextAge) => age + nextAge.age, 0) / userData.length; return Math.round(average); };

console.log(averageAge());