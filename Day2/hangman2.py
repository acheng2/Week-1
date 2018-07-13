import random
def d6():
    print("__________")
    print("|        |")
    print("|       ( )")
    print("|       /|\ ")
    print("|        | ")
    print("|       / \ ")
    print("|")
    print("_______________")

def d5():
    print("__________")
    print("|        |")
    print("|       ( )")
    print("|       /|\ ")
    print("|        | ")
    print("|       /  ")
    print("|")
    print("_______________")
def d4():
    print("__________")
    print("|        |")
    print("|       ( )")
    print("|       /|\ ")
    print("|        | ")
    print("|")
    print("|")
    print("_______________")
def d3():
    print("__________")
    print("|        |")
    print("|       ( )")
    print("|       /| ")
    print("|        | ")
    print("|")
    print("|")
    print("_______________")
def d2():
    print("__________")
    print("|        |")
    print("|       ( )")
    print("|        | ")
    print("|        | ")
    print("|")
    print("|")
    print("_______________")
def d1():
    print("__________")
    print("|        |")
    print("|       ( )")
    print("|")
    print("|")
    print("|")
    print("|")
    print("_______________")

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

print("Welcome to Hangman!")
print("Difficulties: Easy, Medium, Hard")
dif = input("Please choose a difficulty. Put your response in quotes")

list_easy = ["fire", "water", "earth", "air", "light", "stone", "lava"] #wind, poison, lava, metal, void, holy, wood
list_medium = ["lightning", "shadow", "psychic", "spirit", "aether", "quintessence", "demonic"]
list_hard = ["hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen"]


if dif == "Easy":
    easy_num = random.randint(0, len(list_easy) - 1)
    easy_word = list_easy[easy_num]
    print("*" * len(easy_word))

    noOfTries = 0

    blank = "*" * len(easy_word)
    LBlank = list(blank)

    list_hangman = [d1, d2, d3, d4, d5, d6]

    while noOfTries < 6:
        guess = input("Please guess a letter")
        if guess in easy_word:
            indexes = find(easy_word, guess)
            print (indexes)

            for i in indexes:
                LBlank[i] = guess

            print(''.join(LBlank))
        else:
            print("Incorrect!")
            print list_hangman[noOfTries]()
            noOfTries = noOfTries + 1

    if noOfTries == 6:
        print("Game Over!")
    else:
        print("You win!")

if dif == "Medium":
    medium_num = random.randint(0, len(list_medium) - 1)
    medium_word = list_medium[medium_num]
    print("*" * len(medium_word))

    noOfTries = 0

    blank = "*" * len(medium_word)
    LBlank = list(blank)

    list_hangman = [d1, d2, d3, d4, d5, d6]

    while noOfTries < 6:
        guess = input("Please guess a letter")
        if guess in medium_word:
            indexes = find(medium_word, guess)
            print (indexes)

            for i in indexes:
                LBlank[i] = guess

            print(''.join(LBlank))
        else:
            print("Incorrect!")
            print list_hangman[noOfTries]()
            noOfTries = noOfTries + 1

    if noOfTries == 6:
        print("Game Over!")
    else:
        print("You win!")

if dif == "Hard":
    hard_num = random.randint(0, len(list_hard) - 1)
    hard_word = list_hard[hard_num]
    print("*" * len(hard_word))

    noOfTries = 0

    blank = "*" * len(hard_word)
    LBlank = list(blank)

    list_hangman = [d1, d2, d3, d4, d5, d6]

    while noOfTries < 6:
        guess = input("Please guess a letter")
        if guess in hard_word:
            indexes = find(hard_word, guess)

            for i in indexes:
                LBlank[i] = guess

            print(''.join(LBlank))
        else:
            print("Incorrect!")
            print list_hangman[noOfTries]()
            noOfTries = noOfTries + 1

    if noOfTries == 6:
        print("Game Over!")
    else:
        print("You win!")
