#1_________________________________________________
print("{0}\n{0}\n{0}\n{0}".format("Hello World"))

#2_________________________________________________
print((99**3)*8)

#3_________________________________________________
#False
print(5 < 3)

#True
print(3 == 3)

#False
print(3 == "3")

#TypeError
try:
    print("3" > 3)
except TypeError as e:
    print(e)

#False
print("Hello" == "hello")

#4_________________________________________________
computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer")

#5_________________________________________________
name = 'Lidia'
age = 44
shoe_size = 39
info = 'My name is {}, I am {} years old and my shoe size is {}.'.format(name, age, shoe_size)
print(info)

#6_________________________________________________
a = 200
b = 100
if a > b:
    print('Hello World')

#7_________________________________________________
number = input("write a number: ")
num = int(number)

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#8_________________________________________________
name = input("Enter your name: ")
nameL = name.lower()
count = 0

if nameL == "lidia":
    print("Hello, Lidia! You have a beautiful name! Like me!")
else:
    for l in nameL:
        if l in "lidia":
            count += 1  
    if count >= 4:
        print("Hi, {}! We have some same letters in ours names!".format(name))
    elif count == 0:
        print("Hello, {}! Don't be apseade. Your name is lovely too!".format(name))          
            
#9_________________________________________________
print('Welcome to the Roller Coaster!')
height = input("For approved your ride enter your height in inches: ")
height = int(height)

if height * 2.54 > 145:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")     
    