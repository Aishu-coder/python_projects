from random import choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():

    card=choice(cards)
    return card

def winner(p_score, c_score):
    if p_score==c_score :
        return "Draw"
    elif p_score==0:
        return "win with a blackjack."
    elif c_score ==0:
        return "loose,Opponent wins with a blackjack."
    elif p_score >21:
        return "loose ,you went over."
    elif c_score > 21:
        return " Win,Opponent went over."
    elif c_score > p_score:
        return "loose"
    else:
        return " win"

player_cards=[]
computer_cards=[]
computer_score=0
player_score=0
is_game_over=True
for _ in range(2):
    player_cards.append(deal_cards())
    computer_cards.append(deal_cards())

while is_game_over:
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    if player_score == 21 and len(player_cards) == 2:
        player_score=0
    if computer_score==21 and len(player_cards)==2 :
        computer_score=0
    if 11 in player_cards and player_score>21:
        player_cards.remove(11)
        player_cards.append(1)
    print(f"your cards:{player_cards}, current score :{player_score}")
    print(f"computer's first card:{computer_cards[0]}")
    if player_score == 21 or computer_score == 21 or player_score > 21:
        is_game_over = False
    else:
        Ask_for_another_card = input("Type 'y' to get another card 'n' to pass ")
        if Ask_for_another_card == 'y':
            player_cards.append(deal_cards())
            player_score=sum(player_cards)
        else:
            is_game_over = False
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_cards())
        computer_score = sum(computer_cards)
    print(f"your cards:{player_cards}, current score :{player_score}")
    print(f"computer's final hand:{computer_cards},final score:{computer_score}")
    print(winner(player_score,computer_score))
    is_game_over=False