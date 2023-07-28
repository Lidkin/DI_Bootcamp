import re
import os

class AnagramChecker:
    path = os.getcwd()
    red = '\033[31m'
    reset = '\033[0m'

    def __init__(self):
        self.text = AnagramChecker.find_file('sowpods.txt', AnagramChecker.path)

    @staticmethod
    def find_file(filename, path):
        try:
            while True:
                for root, dirs, files in os.walk(path):
                    if filename in files:
                        return os.path.join(root, filename)
                        break
                if path == os.path.dirname(path):
                    raise Exception("Reached the root directory. File not found.")
                    break    
                path = os.path.dirname(path)
        except Exception as err:
            print(err)        

    def is_valid_word(self, word):
        try:
            with open(self.text, 'r') as f:
                text = f.read()
                text_list = text.split('\n')
                if word is not None and word in text_list:
                    return True 
                else:
                    raise Exception    
        except Exception:
            print(f'{AnagramChecker.red}{word}{AnagramChecker.reset} is not a valid English word')
            return False            

    def get_anagrams(self, valid_word):
        user_word = valid_word.upper()
        anagrams_list = []
        with open(self.text, 'r') as f:
            words = f.read().split('\n')
            anagrams_list = [w for w in words if len(w) == len(user_word) and AnagramChecker.is_anagram(user_word, w) and w != user_word]
        return anagrams_list  

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)   