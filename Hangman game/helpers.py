import os 
import platform
import pandas as pd
import random
import re


def clear_screen():
    """This is a Python function clear_screen() that clears the terminal console screen.
    The function uses the os module to determine the operating system and run the 
    appropriate clear command. If the system is Windows, it uses the command os.system('cls') 
    to clear the console screen. Otherwise, it uses the command os.system('clear') 
    to clear the console screen in other operating systems (e.g., Linux, macOS).
    This function is useful to make the game's display more user-friendly by clearing 
    the console screen and avoiding cluttered output."""

    os.system('cls') if platform.system() == 'Windows' else os.system('clear')

def category_selection(option):
    """This Python code defines a function `category_selection(option)` that selects 
    a word from a predefined list of animals or countries based on the option argument 
    provided to the function. If `option` is "animal", the function reads the animals.csv 
    file using pandas' `read_csv()` method, extracts the second column (animals' names), skips 
    the first row (header), and returns a randomly selected animal name as a lowercase string.
    It also counts the number of unique letters in the chosen animal name and returns 
    it as a second value. If `option` is "country", the function reads the countries.csv file 
    using pandas' `read_csv()` method, extracts the first column (countries' names), 
    skips the first row (header), and returns a randomly selected country name as a lowercase string.
    It also counts the number of unique letters in the chosen country name and returns it as a second value.
    The function uses the `random` module to randomly select an item from the list of animals or countries. 
    The `set()` function is used to get a set of unique letters in the selected word, and the `discard()` 
    method is used to remove the space character from the set, so it doesn't count as a unique letter.
    This function is used to select a word from a predefined list of categories to be used
    in the Hangman game."""

    if option == "animal":        
        reader = pd.read_csv("animals.csv", usecols=[1],skiprows=[0], encoding="utf-8").values.tolist() 
        hidden_animal = random.choice(reader)
        unique_letters = set(hidden_animal[0].lower())
        unique_letters.discard(" ")        
        return hidden_animal[0].lower(), len(unique_letters)
    elif option == "country":
        reader = pd.read_csv("countries.csv", usecols=[0],skiprows=[0], encoding="utf-8").values.tolist() 
        hidden_country = random.choice(reader)
        unique_letters = set(hidden_country[0].lower())
        unique_letters.discard(" ")
        return hidden_country[0].lower(), len(unique_letters)
    
def ask_letter(): 
    """This Python code defines a function `ask_letter()` 
    that prompts the user to choose a letter and returns the letter as a lowercase string.
    The function uses a while loop that runs indefinitely until the user inputs a 
    valid letter. The `input()` function is used to prompt the user to enter a letter, 
    which is then converted to lowercase using the `lower()` method. 
    The `re.match()` function is used to validate that the input is a single lowercase 
    letter between a and z. If the input matches the regular expression `[a-z]$`, 
    the function breaks out of the loop and returns the chosen letter. 
    If the user enters an invalid input that does not match the regular expression, 
    the function will display an error message by calling the `clear_screen()` function 
    and then print the message "Please, choose a correct letter" to prompt the user to try again."""

    while True:
        chosen_letter = input("Choose a Letter: ").lower()
        if re.match('[a-z]$',chosen_letter):                   
            break
        else:
            clear_screen()
            print("Please, choose a correct letter")
    return chosen_letter
        
def board(hidden_word, correct_letters):
    """This Python code defines a function `board(hidden_word, correct_letters)` that prints 
    the current state of the hidden word with correct guessed letters replaced by their actual 
    letter and unknown letters replaced by dashes ("-"). It takes two arguments:
    - `hidden_word`: a string representing the hidden word.
    - `correct_letters`: a list of lowercase letters representing the correct guessed letters.
    The function creates an empty list `hidden_list` and iterates over each letter `l` in the `hidden_word`.
    If `l` is in `correct_letters`, it appends it to `hidden_list`. If `l` is a space, it appends 
    a forward slash ("/") to `hidden_list`. Otherwise, it appends a dash ("-") to `hidden_list").
    After the loop, the function prints the `hidden_list` joined with spaces using the `join()` 
    method with a space character as the separator. The resulting output is the current state 
    of the hidden word with dashes representing unknown letters and the correct guessed 
    letters in their corresponding positions."""

    hidden_list = []
    
    for l in hidden_word:
        if l in correct_letters:
            hidden_list.append(l)
        elif l == " ":
            hidden_list.append("/")            
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))    

def check_letter(choosen_letter, hidden_word, correct_letters, incorrect_letters, attempts, hits):
    """This is a Python function called `check_letter()` that receives 6 arguments:
    `choosen_letter`, `hidden_word`, `correct_letters`, `incorrect_letters`, `attempts`, and `hits`.
    This function is responsible for checking if the letter chosen by the user `choosen_letter` 
    is present in the `hidden_word`. If it is, the function checks whether the letter has already 
    been guessed correctly and, if not, adds it to the list of `correct_letters`. 
    The function also updates the `hits` variable to count the number of correct letters that have 
    been guessed. If the `choosen_letter` is not in the `hidden_word`, it is added to the list 
    of `incorrect_letters`. The function also decreases the number of `attempts` left by one.
    Finally, the function returns the updated values of `attempts` and `hits`."""
    
    if choosen_letter in hidden_word and choosen_letter not in correct_letters:
        correct_letters.append(choosen_letter)
        hits += 1
    elif choosen_letter in hidden_word and choosen_letter in correct_letters:
        pass
    else:
        incorrect_letters.append(choosen_letter)
        attempts -= 1

    return attempts, hits


          
        
    

    
   
