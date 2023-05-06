import helpers

def start():
    """This is a Python code for a Hangman game menu initializer. 
    It includes a loop that allows the user to choose from three options: 
    animals, countries or close the game. Once the user selects a category, 
    the program will generate a hidden word from that category and display 
    the user's progress in guessing the letters of the word.
    The user has 10 attempts to guess the word, and each incorrect guess 
    will reduce the number of remaining attempts. 
    The program will display the correct and incorrect letters that the user 
    has guessed so far, as well as a visual representation of the Hangman game board.
    If the user guesses all the unique letters of the hidden word before 
    running out of attempts, the program will congratulate the user. 
    If the user runs out of attempts without guessing the word, the program 
    will reveal the hidden word and inform the user that they have lost the game.
    After the user completes a game, the program will prompt the user 
    to press ENTER to continue or start a new game by selecting a category."""   

    while True:

        incorrect_letters = []
        correct_letters = []
        attempts = 10
        hits = 0

        helpers.clear_screen()

        print("===============================")
        print(" Welcome to Hangman [CSprog87] ")
        print("===============================")
        print("   Choose a category to play   ")
        print(">[1] Animals                   ")
        print(">[2] Countrys                  ")
        print(">[3] Close the game            ")
        print("===============================")

        option = input("--> ")
                
        if option == "1":
            category = "animal"                         
            hidden_word, unique_letter = helpers.category_selection(category)                                 
            while True:                
                helpers.clear_screen() 
                print(f"You have {attempts} remaining attempts")
                print(f"Correct letters: {set(correct_letters)}")
                print(f"Incorrect letters: {set(incorrect_letters)}")
                helpers.board(hidden_word, correct_letters)  
                print(hits, unique_letter)              
                letter = helpers.ask_letter() 
                attempts, hits = helpers.check_letter(letter,hidden_word,correct_letters,incorrect_letters,attempts,hits)
                
                if attempts == 0:
                    print(f"Sorry, you have not found the word: {hidden_word.capitalize()}")
                    break
                elif hits == unique_letter:
                    print(f"Congratulations, you have found the word: {hidden_word.capitalize()}")
                    break           
            
        elif option == "2":
            category = "country"
            hidden_word, unique_letter = helpers.category_selection(category)                               
            while True:                
                helpers.clear_screen() 
                print(f"You have {attempts} remaining attempts")
                print(f"Correct letters: {set(correct_letters)}")
                print(f"Incorrect letters: {set(incorrect_letters)}")
                helpers.board(hidden_word, correct_letters)  
                print(hits, unique_letter)              
                letter = helpers.ask_letter() 
                attempts, hits = helpers.check_letter(letter,hidden_word,correct_letters,incorrect_letters,attempts,hits)
                
                if attempts == 0:
                    print(f"Sorry, you have not found the word: {hidden_word.capitalize()}")
                    break
                elif hits == unique_letter:
                    print(f"Congratulations, you have found the word: {hidden_word.capitalize()}")
                    break           
           
        elif option == "3":
            print("Leaving the game...")
            break
        else:
            print("Please select a valid option") 

        input("\nPresiona ENTER para continuar...")
            
    

