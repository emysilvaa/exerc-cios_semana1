"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

turtle = turtle.Turtle()

for _ in range(4):
   turtle.shape('turtle')
   turtle.color('red')
   turtle.forward(100)
   turtle.right(90)

for _ in range(4):
   turtle.shape('triangle')
   turtle.color('green')
   turtle.left(90)
   turtle.forward(100)

for _ in range(4):
   turtle.shape('circle')
   turtle.color('yellow')
   turtle.forward(100)
   turtle.left(90)

for _ in range(4):
   turtle.shape('arrow')
   turtle.color('purple')
   turtle.right(90)
   turtle.forward(100)

