let client = "John";

const groceries = {
    fruits: ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice: "20$",
    other: {
        paid: true,
        meansOfPayment: ["cash", "creditCard"]
    }
}

const displayGroceries = () => groceries.fruits.forEach((fruit) => console.log(fruit));
displayGroceries();

const cloneGroceries = () => {
    let user = client;
    client = 'Betty';

    console.log(user, client);
    console.log(groceries);

    const shopping = groceries;
    shopping.totalPrice = '35$';
    shopping.other.paid = false;

    console.log(groceries, shopping);
};

cloneGroceries();