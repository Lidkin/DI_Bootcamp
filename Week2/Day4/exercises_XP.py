import random

#1______________________________________________
display_message = lambda s : print(s)

display_message("I learning html, css, javascript and Python in this course")

#2______________________________________________
favorite_book = lambda title: print(f"One of my favorite books is {title}.")  

favorite_book('"It"')

#3______________________________________________
describe_city = lambda city, country='austria': print(f"{city.title()} is in {country.title()}.")
describe_city('vienna')

#4______________________________________________
def compare_numbers(random_number, user_number):
    if random_number == user_number:
        print("You guessed right!")
    else:
        print(f"You guessed wrong!\n{user_number} - {random_number}")

while True:
    user_number = int(input("Enter a number between 1 and 100: "))

    random_number = 56

    compare_numbers(random_number, user_number)
    print('wanna play again? (y/n)')
    if input() == 'n':
        break

#5______________________________________________
make_short = lambda size='L', text='"I love Python"' : print(f"The size of the shirt is {size} and the text is {text}")

make_short()
make_short('M')    
make_short(size='S', text='"javascript forever"')

short = {'size': 'XS', 'text': '"I love C#"'}
make_short(**short)

#6______________________________________________
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magician_names):
    great = lambda s: f"The Great {s}"
    return list(map(great, magician_names))

magician_names = make_great(magician_names)
show_magicians(magician_names)             

#7______________________________________________

def get_random_temp(month):
    if month == 12 or month in range(1, 3):
        return random.uniform(-10.0, 11.0), 'winter'
    if month in range(3, 6):
        return random.uniform(17.0, 24.0), 'spring'        
    elif month in range(6, 9):
        return random.uniform(25.0, 40.0), 'summer'
    elif month in range(9, 12):    
        return random.uniform(12.0, 20.0), 'autumn'

def main():
    month = int(input("Enter number of month: "))
    temp_season = get_random_temp(month)
    temp = float('{:.2f}'.format(temp_season[0]))
    season = temp_season[1].capitalize()
    if temp < 0:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nBrrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nQuite chilly! Don't forget your coat.") 
    elif temp < 24:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nIt's a lovely day! Wear whatever you want.")  
    elif temp < 33:   
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nIt's hot! Wear something light. And don't forget to drink plenty of water.")
    else:
        print(f"{season}!\nThe temperature right now is {temp} degrees Celsius.\nIt's sweltering! Stay inside and drink plenty of water.") 

main()
          
#8______________________________________________
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def check_answer(question, answer):
    count_wrong = 0
    correct_answer = 0
    input_value = str(input(question + "\n"))
    if input_value.lower() == answer.lower():
        correct_answer = 1
    else:
        count_wrong = 1
    return correct_answer, count_wrong, input_value

while True:
    correct = 0
    incorrect = 0
    wrong_list = []
    for item in data:
        check = check_answer(item.get("question"), item.get("answer"))
        correct += check[0]
        incorrect += check[1]
        wrong_list.append("Q: {}\n answer: {}| your answer: {}\n".format(item.get("question"), item.get("answer"), check[2]))

    result = '\n '.join(wrong_list) 
    print(f"Correct answers: {correct}\nIncorrect answers: {incorrect}\n{result}")
    if incorrect >= 3:
        input_value = input("Play again! (y/n):")
        if input_value == "y":
            continue
        else:
            break
    else:
        break         