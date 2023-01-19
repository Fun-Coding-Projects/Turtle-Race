"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
from turtle import Screen
import turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title='Make your bet...',
    prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for num, color in enumerate(colors):
    t = turtle.Turtle(shape='turtle')
    t.penup()
    t.goto(x=-230, y=25 * num - 60)
    t.color(color)

screen.exitonclick()
