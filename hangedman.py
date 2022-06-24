#!/usr/bin/env python3
from imp import reload
import random
import os

banner = '''
███████ ██ ████████       ███████ ██ ████████  ██████  ██    ██ ███    ██ ███████       ██
   ███  ██    ██             ███  ██    ██    ██    ██ ██    ██ ████   ██ ██            ██
  ███   ██    ██            ███   ██    ██    ██    ██ ██    ██ ██ ██  ██ █████         ██
 ███    ██    ██           ███    ██    ██    ██    ██ ██    ██ ██  ██ ██ ██
███████ ██    ██          ███████ ██    ██     ██████   ██████  ██   ████ ███████       ██

*******************************************************************************************
*                            Copyright of Hamza MOUNIR, 2022                              *
*                             https://github.com/ZITZITOUNE                               *
*******************************************************************************************
'''

banner2 = '''                                                                                   
                                                                                      +---+    
██   ██  █████  ███    ██  ██████  ███████ ██████   ███    ███  █████  ███    ██  ██  |   |
██   ██ ██   ██ ████   ██ ██       ██      ██   ██  ████  ████ ██   ██ ████   ██  ██  O   |
███████ ███████ ██ ██  ██ ██   ███ █████   ██   ██  ██ ████ ██ ███████ ██ ██  ██  ██  /|\  |
██   ██ ██   ██ ██  ██ ██ ██    ██ ██      ██   ██  ██  ██  ██ ██   ██ ██  ██ ██      / \  |
██   ██ ██   ██ ██   ████  ██████  ███████ ██████   ██      ██ ██   ██ ██   ████  ██      |
                                                                                    ========
'''

# clear
def clear_screen():
    # for windows OS
    if os.name == "nt":
        os.system("cls")

        # for linux / Mac OS
    else:
        os.system("clear")

# colored text and background
def colorRed(clr): print("\033[91m {}\033[00m".format(clr))
def colorGreen(clr): print("\033[92m {}\033[00m".format(clr))
def colorYellow(clr): print("\033[93m {}\033[00m".format(clr))
def colorLightPurple(clr): print("\033[94m {}\033[00m".format(clr))
def colorPurple(clr): print("\033[95m {}\033[00m".format(clr))
def colorCyan(clr): print("\033[96m {}\033[00m".format(clr))
def colorLightGray(clr): print("\033[97m {}\033[00m".format(clr))
def colorBlack(clr): print("\033[98m {}\033[00m".format(clr))
def colorReset(clr): print("\033[0m {}\033[00m".format(clr))


# open file with word
with open("mot_pendu.txt", "r") as file:
    file = file.read()
    choix = list(map(str, file.split()))

# reproduction execfile python2
def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)

# select random word from file
def selectRandom(choix):
    return random.choice(choix)


clear_screen()
colorRed(banner)
colorCyan(banner2)

# select choise of user, play or add word to the dictionnary
if input('PRESS ANY KEY TO PLAY / PRESS 2 TO ADD A WORD TO THE DICTIONARY :') == '2':
    file = open("word_hangedman.txt", "r+")
    new_word = input("Enter word  : ")
    if(new_word in file.read()):
        colorRed("The word already exists ! ")
    else:
        colorGreen("The word has just been added ! ")
        file.write("\n" + new_word)
        file.close()

# game launch
else:
    solution = selectRandom(choix)
    length = str(len(solution))
    attempt = 7
    display = ""
    letters_found = ""

    for l in solution:
        display = display + "_ "

    colorCyan(">> Welcome to the hangman game ! <<")
    colorCyan(">> The word is " + length + " characters. <<")

    while attempt > 0:
        print("\n Word to guess : ", display)
        proposition = input("Submit a letter : ")[0:1].lower()

        if proposition in solution:
            letters_found = letters_found + proposition
            colorGreen("-> YES ! \n")
        else:
            attempt = attempt - 1
            colorRed("-> NO ! \n")
            if attempt == 0:
                colorRed(" ==========Y= ")
            if attempt <= 1:
                colorRed(" ||/       |  ")
            if attempt <= 2:
                colorRed(" ||        0  ")
            if attempt <= 3:
                colorRed(" ||       /|\ ")
            if attempt <= 4:
                colorRed(" ||       /|  ")
            if attempt <= 5:
                colorRed("/||           ")
            if attempt <= 6:
                colorRed("==============\n")

        display = ""
        for x in solution:
            if x in letters_found:
                display += x + " "
            else:
                display += "_ "

        if "_" not in display:
            colorGreen(">>> WINNNNN ! <<<")
            colorGreen(">>> The word was " + solution + " ! <<<")

            break

    print("\n    FINISH !    ")
    answer = str(input('Run again? (y/n): '))
    if answer == 'n':
        print('Goodbye')
    elif answer == 'y':
        # execute the file
        execfile("hangedman.py")
    else:
        print('Invalid input.')
