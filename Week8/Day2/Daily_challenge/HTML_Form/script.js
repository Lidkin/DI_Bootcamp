
inputform.addEventListener('submit', toJson);

function toJson(event) {
    event.preventDefault();
    const h2 = document.createElement('h2');
    h2.innerText = JSON.stringify({ name: event.target.fname.value, lastname: event.target.lname.value });
    document.body.appendChild(h2);
}