import random

list=["nani","aishwarya","apple","mango","anju","aruna"]

choice=random.choice(list)
print(choice)
guess=input('guess a letter : ').lower()
for l in choice :
    if l==guess :
        print("right")
    else :
        print('wrong')
