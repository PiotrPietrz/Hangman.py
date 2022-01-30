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


clues = list(english_words_lower_alpha_set) # get the list of english words

print("\nThere are {} possible clues.\n"
      "The longest word has {} characters".format(len(clues), len(max(clues, key=len))))  # just info

difficulty = int(input("\nChoose the level of difficulty (1 - 3): "))

if difficulty > 3 or difficulty < 1:
    print("\nYou must enter 1, 2 or 3. Please start again.")  # will terminate the program when
    quit()                                                    # the difficulty is not 1, 2 or 3
else:
    clue = give_word(clues, difficulty)
    errors_allowed = len(clue) - 1
    print("\nThe word is {} char long and you can have {} tries.".format(len(clue), errors_allowed + 1))
    print("\nREMEMBER TO INPUT ONLY LOWER_CASE CHARACTERS")

tries_count = 0
blanks = list("_"*len(clue))
attempt = 1
used_letters = set() # set for storing used characters

while tries_count <= errors_allowed and blanks != list(clue):
    print("\nAttempt No. {}. Number of mistakes: {}.".format(attempt, tries_count))

    if attempt > 1:
        print("Used letters: {}".format(used_letters))

    guess = input("Input a character: ")

    # check if the letter was already used
    if guess in used_letters:
        print("This letter was already used!")
        tries_count += 1  # this counts how many failed attempts there were
    # if the letter in guess was not used, check if it occurs in the clue
    else:
        if guess in clue:
            blanks = [guess if letter == guess else blank for blank, letter in zip(blanks, clue)]
            used_letters.add(guess)
            print(''.join(blanks))
        else:
            used_letters.add(guess)
            print(''.join(blanks))
            tries_count += 1  # this counts how many failed attempts there were

    attempt += 1  # this counts how many overall attempts there were

if blanks == list(clue):
    print("\nCongratulations")
else:
    print("\nThe correct word was {}".format(clue))
