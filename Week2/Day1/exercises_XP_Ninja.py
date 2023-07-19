#4_________________________________________________
my_text = "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

#5_________________________________________________
old_sentence = 0

while True:

    sentence = (input('Please, input the longest sentence you can without the character “A” (or "q" for exit): ')).lower()

    if sentence == 'q':
        break
    else:
        if 'a' in sentence:
            print("The caracter 'A' is here! Tray again!")
        else:
            if len(sentence) > old_sentence:
                print("Congratulations! You've just entered the longest sentence ({} long) without the character “A”".format(len(sentence)))
                old_sentence = len(sentence)
            else:
                print('Your sentence must be {} longer. Try again!'.format(old_sentence-len(sentence))) 