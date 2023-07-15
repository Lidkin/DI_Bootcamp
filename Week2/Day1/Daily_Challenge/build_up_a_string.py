
while True:
    string = input("Enter a string (must be 10 characters long): ")

    if len(string) < 10:
        print("String not long enough")
    elif len(string) > 10:
        print("String too long")
    else:
        print("Perfect string")
        break  

print("First letter: {}, second: {}".format(string[0], string[-1]))    

new_string = ""

for l in string:
    new_string += l
    print(new_string)