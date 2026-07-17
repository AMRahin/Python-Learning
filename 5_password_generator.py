import random
import string

print("Wellcome to the password generator!")
how_much_letter=int(input("How much letter would you like?\n"))
how_much_symbol=int(input("How much letter would you like?\n"))
how_much_number=int(input("How many numbers would you like?\n"))

all_letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
all_numbers=["0","1","2","3","4","5","6","7","8","9"]
all_symbol=["!","@","#","$","^","*"] 

password=[]

for letters in range(1,how_much_letter+1):
   
    password+=random.choice(all_letters)

for symbols in range(1,how_much_symbol+1):
     password+=random.choice(all_symbol)

for numbers in range(1,how_much_number+1):
     password+=random.choice(all_numbers)
shuffled_password=random.shuffle(password)
print(f"The Generated password\n{"".join(password)}")


