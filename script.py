from english_words import english_words_lower_alpha_set
import random


def give_word(clues, difficulty):

    """
    The function will pick a random word which length satisfies given parameters
    Difficulty 1: len <= 8
    Difficulty 2: 8 < len <= 14
    Difficulty 3: 14 < len
    """

    if difficulty == 1:
        guessed = 0
        while guessed == 0:
            pick = random.choice(clues)
            if len(pick) <= 8:
                return pick
    elif difficulty == 2:
        guessed = 0
        while guessed == 0:
            pick = random.choice(clues)
            if len(pick) > 8 and len(pick) <= 14:
                return pick
    else:
        guessed = 0
        while guessed == 0:
            pick = random.choice(clues)
            if len(pick) > 14:
                return pick


clues = list(english_words_lower_alpha_set) #get the list of english words

print("There are {} possible clues.\n"
      "The longest word has {} characters".format(len(clues), len(max(clues, key=len)))) #just info

difficulty = int(input("Choose the level of difficulty (1 - 3): "))

if difficulty > 3 or difficulty < 1:
    print("\nYou must enter 1, 2 or 3. Please start again.") #will terminate the program when
    quit()                                                  #the difficulty is not 1, 2 or 3
else:
    clue = give_word(clues, difficulty)
    errors_allowed = len(clue)
    print("The word is {} char long and you can have {} tries.".format(len(clue), errors_allowed))
    print("\nREMEMBER TO INPUT ONLY LOWER_CASE CHARACTERS")

tries_count = 0
blanks = list("_"*len(clue))

while tries_count <= errors_allowed and blanks != list(clue):

    guess = input("Input a character: ")

    if guess in clue:
        blanks[clue.index(guess)] = guess
        print(''.join(blanks))
    else:
        print(''.join(blanks))
        tries_count += 1