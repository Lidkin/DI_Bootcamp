import re

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


        