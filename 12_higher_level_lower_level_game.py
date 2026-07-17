import random
game_data = [
    {"name": "Cristiano Ronaldo", "description": "Footballer", "country": "Portugal", "score": 600},
    {"name": "Lionel Messi", "description": "Footballer", "country": "Argentina", "score": 480},
    {"name": "Selena Gomez", "description": "Musician and Actress", "country": "United States", "score": 420},
    {"name": "Kylie Jenner", "description": "Reality TV Star and Businesswoman", "country": "United States", "score": 390},
    {"name": "Dwayne 'The Rock' Johnson", "description": "Actor and Professional Wrestler", "country": "United States", "score": 380},
    {"name": "Ariana Grande", "description": "Musician and Actress", "country": "United States", "score": 370},
    {"name": "Kim Kardashian", "description": "Reality TV Star and Businesswoman", "country": "United States", "score": 360},
    {"name": "Beyoncé", "description": "Musician", "country": "United States", "score": 315},
    {"name": "Justin Bieber", "description": "Musician", "country": "Canada", "score": 290},
    {"name": "Taylor Swift", "description": "Musician", "country": "United States", "score": 270}
]
main_asci=r"""██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗     ██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗    ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝    ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗    ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║    ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                                                           
 ██████╗  █████╗ ███╗   ███╗███████╗                                                       
██╔════╝ ██╔══██╗████╗ ████║██╔════╝                                                       
██║  ███╗███████║██╔████╔██║█████╗                                                         
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                                                         
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                                                       
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                                       
                                                                                           """
print(main_asci)
asci=r"""██╗   ██╗███████╗
██║   ██║██╔════╝
██║   ██║███████╗
╚██╗ ██╔╝╚════██║
 ╚████╔╝ ███████║
  ╚═══╝  ╚══════╝
                 """
score=0
life=1
game_over=False

person_a, person_b = random.sample(game_data, 2)

name_a = person_a["name"]
desc_a = person_a["description"]
score_a = person_a["score"]

name_b = person_b["name"]
desc_b= person_b["description"]
score_b = person_b["score"]
def a():
    name_a = person_a["name"]
    desc_a = person_a["description"]
    score_a = person_a["score"]
    return (f"{name_a} {desc_a}")

def b():
    name_b = person_b["name"]
    desc_b= person_b["description"]
    score_b = person_b["score"]
    return (f"{name_b} {desc_b}")

while not game_over:
    score_a = person_a["score"]
    score_b = person_b["score"]
    print(a())

    print(asci)

    print(b())

    choice=input("Who has more followers? Type 'A' or 'B':").lower()

    if choice=="a" and score_a<score_b:
        life-=1
        print(f"You lost:{score}")
        if life==0:
            game_over=True
    elif choice=="a"  and score_a>score_b:
        score+=1
        game_over=False
        print(f"your score:{score}")

        person_a=person_b
        person_b=random.choice(game_data)
        while person_a==person_b:
            person_b=random.choice(game_data)
            
    elif choice=="b" and score_a<score_b:
        score+=1
        game_over=False
        print(f"your score:{score}")

        person_a=person_b
        person_b=random.choice(game_data)
        while person_a==person_b:
            person_b=random.choice(game_data)

    elif choice=="b" and score_a>score_b:
        life-=1
        print(f"You lost:{score}")
        if life==0:
            game_over=True
   