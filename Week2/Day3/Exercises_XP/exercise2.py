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