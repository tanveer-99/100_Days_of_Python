from art import logo
import random
print(logo)

print("Welcome to the number guessing game!")

print("I'm thinking of a number between 1 and 100.")

ranNum = random.randint(1,101)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if difficulty != "hard" and difficulty != "easy":
    difficulty = input("You have typed incorrectly. Type 'easy' or 'hard':").lower()

def check():
    while True:
        try:
            guessedNum = int(input("Make a guess: "))
            break  # Exit the loop if input is an integer
        except ValueError:
            print("Please type a valid number.")

    if guessedNum == ranNum:
        print(f"You got it. The answer was: {guessedNum}")
        return 1
    elif guessedNum > ranNum:
        print("Too High! \nGuess Again.")
    else:
        print("Too Low! \nGuess Again.")


if difficulty == "easy":
    for i in range(10, -1 , -1):
        if i == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            break
        print(f"You have {i} attempts remaining to guess the number.")
        result = check()
        if result == 1:
            break
else:
    for i in range(5, -1 , -1):
        if i == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            break
        print(f"You have {i} attempts remaining to guess the number.")
        result = check()
        if result == 1:
            break
