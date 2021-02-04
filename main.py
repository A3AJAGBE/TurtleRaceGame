"""This is a racing game using turtle graphics"""
import random
import turtle

screen = turtle.Screen()
screen.title('Turtle Race Game')
screen.setup(width=500, height=400)


colors = ['pink', 'blue', 'green', 'brown', 'red']
posX = -230
posY = -150
race_turtles = []
for color in colors:
    sample = turtle.Turtle(shape='turtle')
    sample.color(color)
    sample.penup()
    posY += 50
    sample.goto(x=posX, y=posY)
    race_turtles.append(sample)

race_start = False

bet = screen.textinput(title='Make your Bet', prompt='Enter the color of the turtle you support')

if bet:
    race_start = True

while race_start:
    for race_turtle in race_turtles:
        if race_turtle.xcor() > 230:
            race_start = False
            winner = race_turtle.pencolor()
            if winner == bet:
                race_turtle.write(f'Good Bet, {winner} turtle won the race.', align="right", font=("Arial", 15, "bold"))
            else:
                race_turtle.write(f'You lost, {winner} turtle won the race.', align="right", font=("Arial", 15, "bold"))
        distance = random.randint(0, 10)
        race_turtle.forward(distance)

screen.exitonclick()
