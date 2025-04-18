import random

list=["nani","aishwarya","apple","mango","anju","aruna"]
display=[]

choice=random.choice(list)
print(choice)

for w in choice :
    display.append("_") #display+="_"
print(display)

endgame= False

while  not endgame :
    guess=input('guess a letter : ').lower()
    for i in range(len(choice)) :
         if choice[i]==guess:
             display[i]=guess
    print(display)
    if "_" not in display:
        endgame=True
        print("you win!")
