# Hangman game

My approach to create a popular Hangman game in Python. The script uses ```english_words``` library for word search.
The ```give_word()``` function picks a word based on a difficulty chosen by the user. Following are what words are included in each difficulty level:
- ✔️ Difficulty 1: len <= 8
- ✔️ Difficulty 2: 8 < len <= 14
- ✔️ Difficulty 3: 14 < len

The number of :x: errors is determined by the lenght of the words. Should the number be exceded, the game will have to be started over. The program uses a set to store already used characters and checks whether they were already passed in. Putting a duplicate is considered a mistake therefore it increases the number of failed attempts. 
