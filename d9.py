print("welcome to  secret auction program")
auction = {}


def highest_amount_bidder(auction):
    highest_bid = 0
    for person in auction:
        bid_amount = auction[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
    print(f"The winner is {winner} with a bid of ${highest_bid}")


more_bidder = True
while more_bidder:
    Bidder = input("what is your name?")
    bid = int(input("what's your bid?"))
    auction[Bidder] = bid
    ask = input("Are there any other bidders? type 'yes' or 'no'.")
    bidding = ask.lower()
    if bidding == 'yes':
        print("\n" * 20)
    else:
        more_bidder = False
        highest_amount_bidder(auction)
