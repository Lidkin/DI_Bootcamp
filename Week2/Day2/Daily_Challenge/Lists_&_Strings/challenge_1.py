import re 

while True:
    user_input = input("Enter a number and length ('e' to exit): ")
    list_num = re.split(r"[,/\s]+", user_input)
    list_num.remove(list_num[-1]) if list_num[-1] == "" else None
    list_multiples = []
    if user_input == "e":
        break
    else:
        for i in range(int(list_num[1])):
            list_multiples.append(int(list_num[0]) * (i + 1))
        print(list_multiples)    