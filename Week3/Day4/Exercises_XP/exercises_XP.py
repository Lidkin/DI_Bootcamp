import os

print("======================\nExercise 1:")

from random import choices

def get_words_from_file(file_name) -> list:
    with open(file_name, 'r') as f:
        words = f.read().splitlines()
    return words

def get_random_sentence(length):    
    path = os.path.join("C:/Users/lidia/Documents/Programming/DI_course/DI_bootcamp/Week3/Day4/Exercises_XP/", 'sowpods.txt')
    words = get_words_from_file(path)
    return " ".join(choices(words, k=length)).lower()

def main():
    print("This program build sentence with random words.")
    try: 
        length = int(input("Enter the length of the sentence: "))
        if 20 < length < 2 :
            raise ValueError("The length must be between 2 and 20")
        if type(length) is not int:
            raise TypeError
    except Exception as err:
        print("Error: ", err) 
    else:           
        sentence = get_random_sentence(length)
        print(sentence)   

main() 

print("======================\nExercise 2:")
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

def get_salary(sample) :
    data = json.loads(sample)
    return data['company']['employee']['payable']['salary']

def add_birthday(sample) :
    data = json.loads(sample)
    data['company']['employee']['payable']['birth_date'] = '03/07/1997'
    return data

print(get_salary(sampleJson))  
sampleJson = json.dumps(add_birthday(sampleJson)) 

path = os.path.join("C:/Users/lidia/Documents/Programming/DI_course/DI_bootcamp/Week3/Day4/Exercises_XP/", 'file.json')

with open(path, 'w') as f:
    f.write(sampleJson)