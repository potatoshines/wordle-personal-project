import random
from termcolor import colored

MAX_ATTEMPTS = 6

def get_word():
    """Get a random word from a list"""
    with open("wordle_answers.txt", "r") as file:
        return random.choice(file.readlines()).strip()

def print_instructions():
    """Print intructions including MAX ATTEMPTS and Color Codes"""
    print("Welcome to Wordle!\nYou get", MAX_ATTEMPTS, "attempts!\n[Color Codes]")
    print(colored('Green', 'black', 'on_green'), "= Correct Position")
    print(colored('Red', 'black', 'on_light_red'), "= Does Not Exist")
    print(colored('Blue', 'black', 'on_light_blue'), "= Exists, but Incorrect Position\n\n")

def get_guess(attempts):
    """Prompt the user for a guess and validate it."""
    #Get a list of allowed guesses for validation
    with open("allowed_guesses.txt", "r") as fileOne, open("wordle_answers.txt", "r") as fileTwo:
        allowed_guesses = [line.strip() for file in (fileOne, fileTwo) for line in file]

    #Loop until user inputted guess is valid
    while True:
        guess = input(f"Attempt #{attempts}: ").strip().lower()
        if guess in allowed_guesses:
            return guess
        else:
            print("Invalid word.")

def play_wordle(instructions=True):
    """This is the main function to play Wordle"""
    #Print instructions if it's the first time playing
    if instructions: print_instructions()

    attempts = 1
    word = get_word()
    while True:
        guess = get_guess(attempts)
        attempts += 1

        #Evaluate the guess and print updated word display
        output = ""
        correct_guesses = 0
        for i,w in enumerate(guess):
            if w not in word:
                output += colored(" "+w+" ", 'black', 'on_light_red')
            elif guess[i] == word[i]:
                correct_guesses += 1
                output += colored(" "+w+" ", 'black', 'on_green')
            else:
                output += colored(" "+w+" ", 'black', 'on_light_blue')
            output += " "
        print(output)  

        #Check if the word is guessed or the user has ran out of attempts.
        if correct_guesses == 5:
            print("Congrats! You guesses the word.")
            break
        if attempts > 6:
            print("Game Over. You ran out of attempts.")
            print("The word was:", colored(" "+word+" ", 'black', 'on_green'))
            break
    
    #Ask if the user would like to play again.
    play_again = input("Would you like to play again? (y/n)\n")
    if play_again[0] == 'y':
        play_wordle(instructions=False)
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    play_wordle()
