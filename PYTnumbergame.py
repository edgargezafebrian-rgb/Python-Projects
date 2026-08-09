import random

secret_number = random.randint(1, 20)
print("-----------------------")
print("🎲 NUMBER GUESSING GAME")
print("-----------------------")
print("I'm thinking of a number between 1 & 20")
print("You Have 5 Tries To Guess The Number.")
print("Can you guess it?")
if secret_number % 2 == 0:
    print("The Number Is An Even Number!")

else:
    print("The Number Is An Odd Number!")
max_tries = 5
attempt = 0

guess = int(input("Guess the Number"))
attempt = attempt + 1

while guess != secret_number and attempt < max_tries :

    if guess > secret_number:
        print("Too High!")

    elif guess < secret_number:
        print("Too Low!")

    print(f"You Have {max_tries - attempt} Attempt Remaining.")
    guess = int(input("Try Again!"))
    attempt += 1

if guess == secret_number:
    print(f"It Took You {attempt} Tries To Win.")
    print("Nice Guess!")
else:
    print(f"You Had {max_tries} Tries..")
    print("But You Failed To Guess the Number..")
    print(f"Game Over. The Number Was {secret_number} !")
