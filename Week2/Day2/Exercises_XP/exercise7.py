import re

input_fruits = input("Enter your favorite fruit(s): ")
favorite_fruits = re.split(r"[,/\s]+", input_fruits.lower())
favorite_fruits.remove(favorite_fruits[-1]) if favorite_fruits[-1] == '' else None

input_fruit = input("Enter a fruit: ")
if input_fruit.lower() in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it too!")
