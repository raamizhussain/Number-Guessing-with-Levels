import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Easy or Hard: ").lower()
random_num = random.randint(1,100)

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while attempts > 0:
        print(f"You have {attempts} remaining to guess the number!")
        guess = int(input("Make a guess: "))
        if guess == random_num:
            print(f"Correct! {guess}")
            attempts = -1
        elif guess > random_num:
            print("Too High!")
        elif guess < random_num:
            print("Too Low!")
        attempts -= 1
if attempts == 0:
    print("You lost! Out of attempts!")