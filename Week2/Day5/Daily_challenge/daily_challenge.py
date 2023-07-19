#challenge1_______________________________________________________________
#challenge1.1
sequence = input("Enter a sequence of words separated by commas: ")
words = sequence.replace(' ', '')
words = sorted(words.split(','))
print(', '.join(words))

#challenge1.2
sequence = 'without,hello,bag,world'
words = [word for word in sequence.split(',')]
for word in sorted(words):
    if word != words[-1]:
        print(word, end=',')
    else:
       print(word)

#challenge2_______________________________________________________________
def longest_word(text):
    longest = ''
    for word in text.split():
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))