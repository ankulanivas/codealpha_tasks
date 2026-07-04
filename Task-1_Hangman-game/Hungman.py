import random
words = ["python", "batman", "apple", "laptop", "coding"]
computer_word = random.choice(words)
# print(computer_word)
display=["_"] * len(computer_word)
# print(display)
count=6

print("Welcome to Hungman")
print("Guess the word.")


while True:
    print(f"Current word : "," ".join(display))
    guess=input("Enter Your guess : ")

    if len(guess) != 1 or not guess.isalpha():
     print("Please enter a single alphabet.")
     continue

    if guess in computer_word:
       
     for index, letter in enumerate(computer_word):

      if letter == guess:
        display[index] = guess
     
    else:
        print("Wrong Guess")
        count-=1
        print(f"guessess remaining : {count}")    
    
    if "_" not in display:
       print("Congratulations,you guessed it right",end=":")
       print(computer_word)
       break

    if(count==0):
        print("GAME OVER")
        print(f"Correct Word is : {computer_word}")
        break
    