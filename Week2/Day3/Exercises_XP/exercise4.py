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