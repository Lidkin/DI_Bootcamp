import re

cost = 0
print("Welcome to the cinema!")

print("Movie for family!")
while True:
    age = input("Enter age person who wants a ticket or 'q' to exit: ")
    if age == "q":
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        cost += price
print(f"Total cost: {cost}. Enjoy your movie!")      

print('=================\nMovie for adults!')

input_names = input("Enter names of persons who want to buy a tickets: ")
list_of_teenagers = re.split(r"[,/\s]+", input_names.lower())
list_of_teenagers(list_of_teenagers[-1]).remove() if list_of_teenagers[-1] == "" else None
permitted_list = []

for i in list_of_teenagers:
    input_age = int(input(f"{i.capitalize()}, enter youre age: "))
    if input_age > 21:
        permitted_list.append(i.capitalize())

formatted_string = ', '.join(permitted_list)        
print(f"Persons who can buy a tickets: {formatted_string}")
        
