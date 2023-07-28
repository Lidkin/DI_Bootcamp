from anagram_checker import AnagramChecker
import re

cyan = '\033[36m'
magenta = '\033[35m'
green = '\033[32m'
color = '\033[33m'

def menu():
    user = ['w', 'x']
    print(f"_____________________\nMenu:\n{green}({user[0]}){AnagramChecker.reset} Input word\n{AnagramChecker.red}({user[1]}){AnagramChecker.reset} Exit")
    try:
        user_input = input(f"Your choice {cyan}=>{AnagramChecker.reset} ")
        if user_input == user[1]:
            user_input = None
        elif user_input == user[0]:
            user_input = user_choice()
        else: 
            raise Exception    
    except Exception as err:
        print(err) 
    return user_input       

def user_choice():
    pattern = r'[\D]'
    try:
        word = input('Enter your word: ')
        if re.match(pattern, word) and len(re.split(r'[\s]', word)) < 2 :
            return re.sub(r'[^a-zA-Z]', "", word).upper()
        else:
            raise Exception
            
    except Exception as err:
        print('Should be only one word!')
    finally:
        print('-----------------')     

def main():
    word = menu()
    if word:
        print(f'Your word is {color}{word.upper()}{AnagramChecker.reset}')
        a = AnagramChecker()
        if a.is_valid_word(word):
            print(f'{green}This is a valid English word{AnagramChecker.reset}\nAnagrams for your word are:')
            print(magenta + f'{AnagramChecker.reset}, {magenta}'.join(a.get_anagrams(word)).lower() + AnagramChecker.reset)
            main()

main()               