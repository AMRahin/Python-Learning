import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    chosen_card=random.choice(cards)
    return chosen_card
def calculate_score(cards):
    score=sum(cards)
    if score==21 and len(cards)==2:
        return 0
    if score>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score=sum(cards)
    
    return score
def compare(user_score, computer_score):
    
    if user_score == computer_score:
        return "Draw! "
    
   
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack! "
        
   
    elif user_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win! "
        
    
    elif user_score > computer_score:
        return "You win! "
    else:
        return "You lose "
another_card=True 

score=0  
user_cards=[]
computer_cards=[]

for _ in range(2):
    user_cards.append(deal_card())

    computer_cards.append(deal_card())



game_over = False

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
        
    else:
        user_choice = input("Do you want another card? 'y' or 'n': ").lower()
        if user_choice == "y":
            user_cards.append(deal_card())
        else:
            game_over = True




while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    
    computer_score = calculate_score(computer_cards)

print(f"\nFinal Player Hand: {user_cards}, Final Score: {user_score}")
print(f"Final Computer Hand: {computer_cards}, Final Score: {computer_score}")

print(compare(user_score, computer_score))
