"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle
import random
colors = ['pink', 'black', 'purple', 'blue', 'yellow','brown', 'green' ]
turtle = turtle.Turtle()
turtle.shape('turtle')

for c in range(360):
    color = random.choice(colors)
    turtle.speed(50)
    turtle.color(color)
    turtle.pensize(5)
    turtle.forward(3)
    turtle.right(1)
