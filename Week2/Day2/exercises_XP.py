import re

#1_______________________________________________
my_fav_numbers = {22, 99, 15, 5, 100}
my_fav_numbers.add(19)
my_fav_numbers.add(89)
print(my_fav_numbers)

friend_fav_numbers = {5, 19, 30, 33, 100}

# Because set is unorderd collection we can't now which number is the last one
# There are three options for deleting the last number
# 1. Remove number which added last
my_fav_numbers.remove(89)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Set without number which was added last: {}".format(my_fav_numbers))
print("our favorite numbers: {}".format(our_fav_numbers))
# return the removed number
my_fav_numbers.add(89)

# 2. remove an arbitrary element
my_fav_numbers.pop()
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print("Set without arbitrary element: {}".format(my_fav_numbers))
print("our favorite numbers: {}".format(our_fav_numbers))
# return the removed number
my_fav_numbers.add(99)

# 3. remove biggest number
my_fav_numbers.remove(max(my_fav_numbers))
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print("Set without biggest number {}".format(my_fav_numbers))
print("our favorite numbers: {}".format(our_fav_numbers))

#2______________________________________________
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

try:
    my_tuple.add(6)
    print("6 was added using add(): ", str(my_tuple))

except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple += (6,)
    print("6 was added using concatenation of tuples:", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple += (6)
    print("6 was added using concatenation of tuple and int: ", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple.append(6)
    print("6 was added using append(): ", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

try:
    my_tuple.extend(6)
    print("6 was added using extend(): ", str(my_tuple))
except Exception as e:
    print("Can't add 6 to tuple. Error:", str(e))

#3___________________________________________________
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

apples = basket.count("Apples")
print(apples)

basket.clear()
print(basket)

#4____________________________________________________
# Float is a data type that represents real numbers with fractional parts.
# Integers are whole numbers without any fractional part, while floats can represent both whole numbers and numbers with decimal places.

my_floats_list = []
k = 1.0

for i in range(9):
    my_floats_list.append(k)
    k += 0.5

print(my_floats_list)

# ++++++++++++++++++++++++++++++++++++++++
start = 1.0
stop = 5.5
step = 0.5

for i in range(int((stop - start)/step)):
    my_floats_list[i] = start + i * step
# other_floats_list = [start + i * step for i in range(int((stop - start)/step))]
print(my_floats_list)

#5____________________________________________________
for i in range(1, 21):
    print(i)

my_list = [i for i in range(1, 21)]
print(my_list)

for i in range(1, 21, 2):
    print(i)

even_idx_list = [i for i in range(1, 21, 2)]
print("Those elements has an even index:", str(even_idx_list))

even_int_list = [i for i in range(2, 21, 2)]
print("Those integers is even:", str(even_int_list))

#6____________________________________________________
my_name = "lidia"

while True:
    name = input("Enter your name: ")
    if name.lower() == my_name:
        print("Hello, Lidia!")
        break

#7____________________________________________________

input_fruits = input("Enter your favorite fruit(s): ")
favorite_fruits = re.split(r"[,/\s]+", input_fruits.lower())
favorite_fruits.remove(favorite_fruits[-1]) if favorite_fruits[-1] == '' else None

input_fruit = input("Enter a fruit: ")
if input_fruit.lower() in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it too!")

#8____________________________________________________
price = 10

while True:
    input_toping = input("Enter of pizza toppings ('quit' to stop): ")
    if input_toping.lower() == "quit":
        break
    else:
        price += 2.5
        print(f"Adding {input_toping} to your pizza!")

print(f"Your pizza costs {price} NIS.")

#9____________________________________________________

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
        
#10____________________________________________________
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich.lower())

for i in finished_sandwiches:
    print(f"I made your {i}.")
