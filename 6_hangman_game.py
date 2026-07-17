import random

word_list = ["aardvark", "elephant", "flamingo", "zebra", "camel"]
random_word = random.choice(word_list)
word_length = len(random_word)

display = []
for _ in range(word_length):
    display.append("_")

lives = 5
game_over = False

while not game_over:
    print(f"\nWord to guess: {' '.join(display)}")
    print(f"Lives remaining: {lives}")
    
    guess = input("Guess a letter: ").lower()
    
    if guess in random_word:
        for position in range(word_length):
            letter = random_word[position]
            if letter == guess:
                display[position] = letter
        print("Right!")
    else:
        lives -= 1
        print(f"Wrong! '{guess}' is not in the word.")

    
    if lives == 0:
        game_over = True
        print("\n--- GAME OVER ---")
        print(f"You ran out of lives. The word was: {random_word}")

    
    if "_" not in display:
        game_over = True
        print(f"\nWord: {' '.join(display)}")
        print("--- YOU WIN! ---")