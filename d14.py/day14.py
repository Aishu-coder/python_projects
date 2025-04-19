from random import choice
from data import data_celebs
import logo

# randomly selecting 2 person's from the data
A = choice(data_celebs)
B = choice(data_celebs)
if A == B:
    B = choice(data_celebs)
score = 0

correct_ans = False
while not correct_ans:

    print(f"compare A: {A['name']},{A['Description']},{A['country']}'")
    print(logo.vs)
    print(f"Against B: {B['name']},{B['Description']},{B['country']}'")

    # comparing the followers between A and B

    if A['followers_count'] > B['followers_count']:
        win = "A"
    else:
        win = "B"
    # input from the user
    # higher will take the input as the character not as variable
    higher = input("Who has more followers? Type 'A' or 'B'.").upper()

    if higher == win:
        score += 1
        print("\n" * 20)
        print(logo.logo)
        print(f"you're right!,current score:{score}")

        C = choice(data_celebs)
        if win == 'B':
            A = B
            B = C
        elif win == 'A':
            B = C
    else:
        print("\n" * 20)
        print(logo.logo)
        print(f"fail,final score:{score}")
        correct_ans = True
