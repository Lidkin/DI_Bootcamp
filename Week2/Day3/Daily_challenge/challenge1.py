while True:
    word = input("Enter a word: ").lower()

    letters_dict = {}
    prev_letter = None

    for item in enumerate(word):
        if item[1] not in letters_dict:
            letters_dict[item[1]] = []
        letters_dict.get(item[1], []).append(item[0])

    print(letters_dict)

    answer = input("Do you want to continue? (y/n): ").lower()
    if answer == "n":
        break    