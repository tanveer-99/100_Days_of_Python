import random
from hangman_art import stages, logo
from hangman_words import word_list


#start screen
print(logo)
chosen_word = random.choice(word_list)
placeholder = ""
for i in range(0, len(chosen_word)):
    placeholder += "_"
print(placeholder)

lives = 6
game_over = False
already_guessed_letters = []
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in already_guessed_letters:
        print(f"You've already guessed {guessed_letter}.")
    display = ""
    for letter in chosen_word:
        if guessed_letter == letter:
            display += letter
            already_guessed_letters.append(letter)
        elif letter in already_guessed_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess " + display)

    if guessed_letter not in already_guessed_letters:
        lives -= 1
        print(f"Your guessed '{guessed_letter}', that is not in the word. You lose a life!")
        if lives == 0:
            game_over = True
            break

    if "_" not in display:
        print("You Won")
        game_over = True
        break

    print(stages[lives], end='')
    print(f"************************* {lives} lives left *************************")



if lives == 0:
    print(f"***************It was {chosen_word}! You Loose!***************")
