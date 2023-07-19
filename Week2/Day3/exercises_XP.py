#1______________________________________________
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)

#2______________________________________________
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def movie_tickets(family):
    cost = 0
    for age in family.values():
        if age < 3:
            cost += 0
        elif age <= 12:
            cost += 10
        else:
            cost += 15
    return cost

final_cost = movie_tickets(family)
print(f"Family's total cost: {final_cost}$")    

#Bonus:
family = {}
while True:
    value_input = input("Enter family member's name and age separated by space ('e' for exit): ")
    split_input = value_input.split()
    split_input.remove(split_input[-1]) if split_input[-1] == '' else None

    if value_input == 'e':
        break
    else:
        key, value = split_input
        family[key] = int(value)
final_cost = movie_tickets(family)
print(f"Family's total cost: {final_cost}$")   

#3______________________________________________
brand = {}

#2.
brand['name'] = 'Zara'
brand['creation_date'] = 1975
brand['creator_name'] = 'Amancio Ortega Gaona'
brand['type_of_clothes'] = ['men', 'women', 'children', 'home']
brand['international_competitors'] = ['Gap', 'H&M', 'Benetton']
brand['number_stores'] = 7000
brand['major_color'] = dict(zip(['France', 'Spain', 'USA'], ['blue', 'red', ['pink', 'green']]))

for key, value in brand.items():
    print(f"{key}: {value}")

#3.
brand['number_stores'] = 2

#4.
type_of_clothes = 's, '.join(brand['type_of_clothes'])
print(f"Zara's clients are {type_of_clothes}")

#5.
brand['country_creation'] = 'Spain'

#6.
brand.setdefault('international_competitors', []).append('Desigual')

#7. Delete the information about the date of creation
del brand['creation_date']

#8. Print the last international competitor.
print(brand.get('international_competitors')[-1])

#9.
print('Major clothes colors in the US:',', '.join(brand.get('major_color').get('USA')))

#10.
print('Length of the dictionary:', len(brand))

#11
print(brand.keys())

#12
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}

#13
brand.update(more_on_zara)
print(brand)

#14
#after update the value from the source dictionary will overwrite the value in the target dictionary
print(brand.get('number_stores')) 

#4______________________________________________
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}

#1.
for item in enumerate(users):
    disney_users_A[item[1]] = item[0]

print(disney_users_A)    

#2.
disney_users_B = {}
for item in enumerate(users):
    disney_users_B[item[0]] = item[1]

print(disney_users_B)    

#3.
disney_users_C = {}
users.sort()

for item in enumerate(users):
    disney_users_C[item[1]] = item[0]

print(disney_users_C)    

#4.1
new_users = [user for user in users if 'i' not in user]

disney_users_D1 = {}
for item in enumerate(new_users):
    disney_users_D1[item[1]] = item[0]
  
print(disney_users_D1)

#4.2

disney_users_D2 = {}
new_users = []

for user in users:
    if user[0].lower() == 'm' or user[0].lower() == 'p':
        new_users.append(user)

for item in enumerate(new_users):
    disney_users_D2[item[1]] = item[0]

print(disney_users_D2)    