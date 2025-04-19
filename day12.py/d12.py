import random
from d12art import logo

print(logo)
print("Welcome ,To the Number Guessing Game \n "
      "I am thinking of the number between 1 to 100")
num = random.randint(1, 100)
level = input("choose the difficulty level. Type 'easy' or 'hard'.").strip().lower()


def guess(count):
    attempts = True
    while attempts:
        count -= 1
        print(f"You have {count} remaining to guess the number.")
        user_guess = int(input("make a guess"))
        if count == 1:
            print("You run out of guess! you loose ")
            print(f"the number : {num}")
            return
        if user_guess > num:
            print("Too high")
        elif user_guess < num:
            print("Too low")
        elif user_guess == num:
            print("That's correct answer.")
            attempts = False


if level == 'easy':
    guess(11)
else:
    guess(6)
