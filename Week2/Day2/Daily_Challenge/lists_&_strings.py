import re 

#challenge1________________
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

#challenge2________________
while True:
    user_string = input("Enter a string  ('e' to exit): ")
    words_list = re.split(r"[,/\s]+", user_string)
    words_list.remove(words_list[-1]) if words_list[-1] == "" else None
    if user_string == "e":
        break
    else:
        for word in words_list:
            new_word = ""
            prev_char = None
            chars = list(word)
            for char in chars:
                if char != prev_char:
                    new_word += char
                prev_char = char
            print(new_word)   