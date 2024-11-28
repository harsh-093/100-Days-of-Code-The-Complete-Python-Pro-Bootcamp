import random
import hangman_art
import hangman_words

print(hangman_art.logo)
start = input("\nPress ENTER to start.")

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
lives = 6
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Guess the word : " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f" Lives left : {lives}/6 ")
    guess = input("\nGuess a letter: ").lower()
    if guess in chosen_word:
        print(f"You've already guessed {guess}.")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("\nGuess the word : " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"\nTHE WORD WAS {chosen_word}. YOU LOSE !!!")

    if "_" not in display:
        game_over = True
        print(" YOU WIN !!!")

    print(hangman_art.stages[lives])