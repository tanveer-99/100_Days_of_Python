import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(1000, 400)
user_bet = screen.textinput('make your bet', 'which turtle will win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle('turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-475,y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

winner = ''
while is_race_on:
    distance = random.randint(0,10)
    tim = all_turtles[random.randint(0,5)]
    tim.forward(distance)
    if tim.xcor() > 475:
        winner = tim.pencolor()
        is_race_on = False

if winner == user_bet:
    print(f"You guessed in right, {winner} won!")
else:
    print(f"You guessed it wrong, {winner} won!")


screen.exitonclick()
