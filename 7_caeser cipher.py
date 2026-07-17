alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = r"""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
should_continue=True
direction=input("Type 'encode' to encrypt,and 'decode' to decrypt:\n").lower()
text=input("type your text message:\n").lower()
shift=int(input("type the shift number:\n"))
def encrypt(original_text,shift_amount):
    cipher_text=""
    for originaltext in original_text:
        if originaltext not in alphabet:
            cipher_text+=originaltext
        else:

            shifted_position=alphabet.index(originaltext)+shift_amount  
            shifted_position%=len(alphabet)
            cipher_text+=(alphabet[shifted_position])
        
    print(f"cipher text is:{cipher_text}")

def decrypt(original_text,shift_amount):
  
    decrypt_value=""
    for originaltext in original_text:
        if originaltext not in alphabet:
            decrypt_value+=originaltext
        else:
            shifted_position=alphabet.index(originaltext)-shift_amount
            shifted_position%=len(alphabet)
            decrypt_value+=(alphabet[shifted_position])
        
    print(f"decrypted cipher text is:{decrypt_value}")

def caeser(original_text,shift_amount,directionality):
    if directionality=="encode":
        encrypt(original_text=text,shift_amount=shift)
    elif directionality=="decode":
        decrypt(original_text=text,shift_amount=shift)
    else:
        print("invalid input!")
caeser(original_text=text,shift_amount=shift,directionality=direction)

user_willing_to_continue=input('If you need to continue "yes" and if not "no":').lower()

should_continue=True

if user_willing_to_continue=="yes":
    should_continue=True
elif user_willing_to_continue=="no":
    print("Caeser cipher stopped")
while should_continue==True:
    direction=input("Type 'encode' to encrypt,and 'decode' to decrypt:\n").lower()
    text=input("type your text message:\n").lower()
    shift=int(input("type the shift number:\n"))
    caeser(original_text=text,shift_amount=shift,directionality=direction)


