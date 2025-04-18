import random

list=["nani","aishwarya","apple","mango","anju","aruna","name","samantha"]
display=[]

choice=random.choice(list)
print(choice)

for _ in choice :
    display.append("_") #display+="_"
print(display)
lives=6
endgame=False
while  not endgame :
    guess=input('guess a letter : ').lower()
    if guess in display:
        print (guess)
        print('you already guessed this letter')

    for i in range(len(choice)) :
         if choice[i]==guess:
             display[i]=guess
    print(display)

    if guess not in choice:
        lives-=1
        print(f" you guesed the letter {guess},that's not in the word.you loose a life ")
        print(lives)
    if "_" not in display:
        endgame=True
        print("you win!")
    elif lives==0:
        endgame=True
        print(" you loose!")


