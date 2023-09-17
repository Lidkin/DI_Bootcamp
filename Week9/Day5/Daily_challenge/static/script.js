const submitFunc = async (event) => {
    try {
        event.preventDefault();
        const endPoint = document.title.toLowerCase().match('login') ? 'login' : 'register';
        const body = new FormData(event.target);
        const jsonData = {};
        body.forEach((value, key) => {
            jsonData[key] = value;
        });
    
        const options = {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        };
        const res = await fetch(`http://localhost:3000/${endPoint}`, options);
        msg.innerText = Object.values(await res.json());
    } catch (error) {
        console.log(error);
    };
};

const updateSubmitButton = (form) => {
    const submitButton = form.querySelector('button');
    const inputFields = form.querySelectorAll('input');
    const allFieldsFilled = [...inputFields].every((input) => input.value !== '');
    submitButton.disabled = !allFieldsFilled;
};

const attachFormValidation = (form) => {
    form.querySelectorAll('input').forEach((input) => {
        input.addEventListener('input', () => {
            updateSubmitButton(form);
        });
    });
    updateSubmitButton(form);
};

const loginForm = document.querySelector('form');
attachFormValidation(loginForm);
