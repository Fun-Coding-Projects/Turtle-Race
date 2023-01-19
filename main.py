"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
from turtle import Screen, Turtle

from random import randint

race = False 

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title='Make your bet...',
    prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for num, color in enumerate(colors):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=25 * num - 60)
    new_turtle.color(color)
    turtles.append(new_turtle)

if user_bet:
  race = True

while race:
  
  for turtle in turtles:
      if turtle.xcor() > 230:
          race = False
          winning_color = turtle.pencolor()
          if winning_color == user_bet:
              print(f"You've won!!! {winning_color} turtle won the race!")
          else:
              print(f"Sorry, you lost. {winning_color} won the race, not {user_bet}.  Try again.")
      stride = randint(0, 10)
      turtle.forward(stride)
      
  
screen.exitonclick()
