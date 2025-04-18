import random

from d7art import logo, hangman
print(logo)
from d7word import word_list
choice=random.choice(word_list)
display=[]
#print(choice)

for w in choice :
    display.append("_") #display+="_"
print(display)
lives=6
endgame=False
while  not endgame :
    guess=input('guess a letter : ').lower()
    for i in range(len(choice)) :
         if choice[i]==guess:
             display[i]=guess
    print(display)
    if guess not in choice:
        lives-=1
        print(hangman[lives])
        # print day7
        # print(lives)
    if "_" not in display:
        endgame=True
        print("you win!")
    elif lives==0:
        endgame=True
        print(" you loose!")



