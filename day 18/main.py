import turtle
import random
import colorgram
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
color_palettes = [
    # Warm Palette
    "#FF5733", "#FFC300", "#FF6F61", "#FFD700", "#FFB347",

    # Cool Palette
    "#3498DB", "#1ABC9C", "#2ECC71", "#9B59B6", "#5DADE2",

    # Neutral Palette
    "#FFFFFF", "#BDC3C7", "#2C3E50", "#EAE7DC", "#A99F96",

    # Pastel Palette
    "#FADADD", "#D5E8D4", "#D6EAF8", "#E8DAEF", "#FAD7A0",

    # Vibrant Palette
    "#FF5733", "#00FFFF", "#3498DB", "#00FF00", "#FFFF00"
]


# draw a square

# turtle.shape('arrow')
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# draw dashed line
# turtle.shape('turtle')
# for i in range(25):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()




# def draw(sides, angle, palette):
#     while sides>0:
#         turtle.color(random.choice(color_palettes))
#         turtle.forward(50)
#         turtle.right(angle)
#         sides -= 1
#
# for sides in range(3,50):
#     angle = 360/sides
#     draw(sides, angle, sides)


# turtle.shape('turtle')
# directions = [90, 180, 270, 360]
# turtle.pensize(15)
# turtle.speed('fastest')
# for _ in range(200):
#     turtle.color(random.choice(color_palettes))
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))


# draw hirst dot painting
turtle.hideturtle()
turtle.speed('fastest')
turtle.penup()
turtle.colormode(255)
color_list = [(246, 243, 239), (247, 242, 244), (203, 165, 108), (239, 245, 240), (152, 74, 48), (234, 238, 243), (52, 93, 124), (170, 153, 41), (223, 202, 136), (137, 32, 21), (132, 163, 185), (47, 121, 88), (198, 91, 72), (15, 99, 73), (70, 47, 39), (147, 179, 148), (98, 73, 75), (162, 142, 157), (234, 175, 164), (55, 46, 49), (184, 205, 172), (24, 81, 87), (38, 61, 74), (142, 22, 25), (85, 146, 126), (45, 65, 85), (175, 91, 94), (214, 177, 183), (18, 70, 64), (109, 125, 151)]

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)



screen = Screen()
screen.exitonclick()