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
            
            
       
