import os
import random
from words import word_list
from hangman_art import logo, stages
print(logo)
chosen_word = random.choice(word_list)

lives = 6
display = []
for _ in chosen_word:
    display.append('_')

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    word_length = len(chosen_word)
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}. That's not in the word, ypu lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose :(")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])
