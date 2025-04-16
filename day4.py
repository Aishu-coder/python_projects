rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
  _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
sicssor='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
userchoice=int(input("enter 0 for rock and 1 for paper and 2 for sicssor\n"))
if userchoice<0 or userchoice>=3:
    print("you have entered an invalid number.")
else :
    if userchoice==0:
        print(rock)
    elif userchoice==1:
        print(paper)
    else:
        print(sicssor)
    list=[rock,paper,sicssor]
    game=len(list)-1
    comchoice=random.randint(0,game)
    print(f"computer's choose:{comchoice}")
    print(list[comchoice])

    if comchoice > userchoice:
        print("you loose")
    elif userchoice > comchoice:
        print("you win!")
    elif userchoice==comchoice :
        print('you draw')
    elif userchoice==2 and comchoice==0:
        print('you loose!')
    elif comchoice==2 and userchoice==0:
        print("you win!")



