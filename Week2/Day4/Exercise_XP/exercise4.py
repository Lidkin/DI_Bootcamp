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