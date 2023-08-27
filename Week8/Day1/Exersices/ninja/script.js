class Bird {
    constructor() {
        console.log("I'm a bird. 🦢");
    }
}

class Flamingo extends Bird {
    constructor() {
        console.log("I'm pink. 🌸");
        super();
    }
}

const pet = new Flamingo();

pet //'my answer is: I'm pink. 🌸\n I'm a bird. 🦢 . Flamingo extends Bird with constructor with 'I'm a bird' and this phrase (super()) going after 'I'm pink'.

