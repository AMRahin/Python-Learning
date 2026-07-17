import colorgram
import turtle 
import random
def random_color():
    color=random.choice(rgb_colors)
    return color
colors = colorgram.extract(r"c:\learn python\udemy python\15_hirst_painting_project.py\spotpainting.jpg", 30)
rgb_colors = [ (136, 166, 198), (18, 31, 53), (217, 155, 108), (204, 137, 148), (235, 213, 96), (53, 105, 143),(136, 178, 162), (154, 67, 52), (159, 15, 24), (139, 72, 81), (232, 164, 170), (48, 28, 31), (201, 90, 102), (40, 29, 27), (152, 22, 15), (55, 115, 98), (15, 54, 44), (234, 169, 160), (213, 86, 68), (172, 188, 219), (12, 97, 71), (110, 122, 162), (27, 60, 112), (169, 204, 191), (233, 165, 12), (37, 158, 201)]
screen = turtle.Screen()
screen.colormode(255)

print(rgb_colors)
t=turtle.Turtle()
t.hideturtle()
t.setheading(225)
t.color("white")
t.forward(350)
t.color("white")
t.setheading(0)
for _ in range(10):
    for _ in range(10):
            t.dot(20,random_color())
            t.penup()
            t.forward(50)


    t.left(90)
    t.forward(50)
    t.left(90)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
















screen.exitonclick()