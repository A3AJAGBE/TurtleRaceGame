import turtle

screen = turtle.Screen()
screen.title('Turtle Race Game')
screen.setup(width=500, height=400)


colors = ['pink', 'blue', 'green', 'brown', 'red']
posX = -230
posY = -150
for color in colors:
    sample = turtle.Turtle(shape='turtle')
    sample.color(color)
    sample.penup()
    posY += 50
    sample.goto(x=posX, y=posY)

bet = screen.textinput(title='Make your Bet', prompt='Enter the color of the turtle you support')
print(bet)


screen.exitonclick()
