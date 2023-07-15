print('Welcome to the Roller Coaster!')
height = input("For approved your ride enter your height in inches: ")
height = int(height)

if height * 2.54 > 145:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")