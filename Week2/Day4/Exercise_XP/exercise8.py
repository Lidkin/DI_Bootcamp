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
        

