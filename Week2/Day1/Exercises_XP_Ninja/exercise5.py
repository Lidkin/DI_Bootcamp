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