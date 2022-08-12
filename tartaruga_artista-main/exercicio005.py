"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import random
import turtle

turtle = turtle.Turtle()
colors = ['purple', 'blue', 'green', 'orange']

for _ in [1, 2, 3]:
  color = random.choice(colors)
  turtle.color(color)
  turtle.shape('circle')
  turtle.forward(200)
  turtle.right(120)

for _ in [1, 2, 3, 4]:
  color = random.choice(colors)
  turtle.color(color)
  turtle.shape('triangle')
  turtle.forward(200)
  turtle.right(90)
 