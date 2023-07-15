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