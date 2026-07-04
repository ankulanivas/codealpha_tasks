import random

words = ["python", "batman", "apple", "laptop", "coding"]

computer_word = random.choice(words)
display = ["_"] * len(computer_word)
lives = 6

print("Welcome to Hangman")
print("Guess the word.")

while True:

    print("\nCurrent Word:", " ".join(display))

    guess = input("Enter your guess: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in computer_word:

        for index, letter in enumerate(computer_word):
            if letter == guess:
                display[index] = guess

        print("✅ Correct Guess!")

    else:
        print("❌ Wrong Guess!")
        lives -= 1
        print(f"Guesses Remaining: {lives}")

    if "_" not in display:
        print(f"\n🎉 Congratulations! You guessed the word: {computer_word}")
        break

    if lives == 0:
        print("\n💀 GAME OVER!")
        print(f"The correct word was: {computer_word}")
        break