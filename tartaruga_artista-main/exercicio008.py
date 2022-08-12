"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.shape('turtle')

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'brown', 'black']
for _ in range (25):
    color = random.choice(colors)
    turtle.color(color)
    turtle.pensize(9)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(15)

