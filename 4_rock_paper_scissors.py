import random

stone=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
your_choise=int(input("what is your choice,choose 0 for stone,choose 1 for paper and choose 2 for scissors.\n"))
rock_paper_scissors=[stone,paper,scissor]
if(your_choise==0):
    print(stone)
elif(your_choise==1):
    print(paper)
elif(your_choise==2):
    print(scissor)   
else:
    print("Wrong input!")  


computer_choosed_number=random.randint(0,2)
print(f"computer choosed.")
if(computer_choosed_number==0):
    print(stone)
elif(computer_choosed_number==1):
    print(paper)
elif(computer_choosed_number==2):
    print(scissor)        

if(your_choise==computer_choosed_number):
    print("Draw!")
elif(your_choise==0 and computer_choosed_number==1):
    print("Computer won!")    
elif(your_choise==0 and computer_choosed_number==2):
    print("You won!")    
elif(your_choise==1 and computer_choosed_number==0):
    print("You won!")    
elif(your_choise==1 and computer_choosed_number==2):
    print("Computer won!")
elif(your_choise==2 and computer_choosed_number==1):
    print("You win!")   
elif(your_choise==2 and computer_choosed_number==0):
    print("Computer won!")
