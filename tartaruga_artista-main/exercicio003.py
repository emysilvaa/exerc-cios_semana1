"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')
turtle.pensize(10)

for color in ['pink', 'red', 'black', 'blue']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

for color in ['pink', 'red', 'black', 'blue']:
    turtle.color(color)
    turtle.right(90)
    turtle.forward(100)
   

