import random

asci=r"""  ________                                 _____     _______               ___.                 
 /  _____/ __ __   ____   ______ ______   /  _  \    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /  /_\  \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \ /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  / \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/          \/            \/    \/     \/       """
print(asci)


print("welcome to number guessing game!")
print("Iam thinking of a number between 1 to 100.")
chosen_number=random.randrange(1,101)
choice=input("Choose a difficulty 'e' for easy and 'd' for dificulty:")
attempts=0
if choice=="e":
    attempts+=10
if choice=="d":
    attempts+=5
game_start=True
while game_start:
    guess=int(input("Make a guess:"))
    if guess==chosen_number:
        print("Your guess is correct")
        game_start=False
    elif guess<chosen_number:
        print("Too low")
        attempts-=1
    elif guess>chosen_number:
        print("Too high")
        attempts-=1
    
    if attempts==0:
        game_start=False
        print("You lost your chances")
 






    

    

    
