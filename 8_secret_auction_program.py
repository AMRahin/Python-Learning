import os
asciiart="""             ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\           
                        
"""
bids={}

continue_bidding=True
def find_highest_bidder(bidding_dictionary):
    highest_bid=0
    winner=""
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner} with a highest bid of {highest_bid}")

   

while continue_bidding:
    name=input("what is yoour name?:").lower()
    price=int(input("what is your bid?:"))
    bids[name]=price
    should_continue=input('"yes" if there are other bidders or "no" to know the highest bidder:').lower()
    if should_continue=="no":
        continue_bidding=False
        os.system('cls' if os.name=='nt' else 'clear')
        find_highest_bidder(bids)
    elif should_continue=="yes":
        continue_bidding=True
        os.system('cls' if os.name=='nt' else 'clear')
        

    
    




