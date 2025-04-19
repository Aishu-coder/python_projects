import random

print("Welcome,To the Number guessing game!\n"
      "I am thinking of the number between 1 to 100.")
number = random.choice(range(1, 100))

level = input("Choose the difficulty leve.Type 'easy' or 'hard'.").strip().lower()


def Guess(count):
    attempts = True
    while attempts:
        count -= 1
        if count == 0:
            attempts = False
        print(f"You have {count} remaining to guess the number")
        guess = int(input('Make a guess'))

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        elif guess == number:
            attempts = False
            print("That's a correct answer.")


if level == 'easy':
    Guess(11)
elif level == 'hard':
    Guess(6)
