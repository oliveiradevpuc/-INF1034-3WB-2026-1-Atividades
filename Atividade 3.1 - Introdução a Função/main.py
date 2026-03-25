from turtle import *
from random import randint 
t = Turtle()

## BASE (PLANO CARTESIANO)
def cartesiano():
    t.color("black")
    t.forward(300) ## direita
    t.stamp()
    t.goto(00,00)
    t.left(90)
    t.forward(300) ## esquerda
    t.stamp()
    t.goto(0,00)
    t.lt(90)
    t.forward(300) ##cima 
    t.stamp()
    t.goto(0,00)
    t.lt(90)
    t.forward(300) ## baixo
    t.stamp()
    t.lt(90)
## Desenhar um triangulo
def triangulo(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    color= textinput("COR","Digite a cor desejada:")
    t.color(color)
    t.begin_fill()
    t.fillcolor(color)
    t.begin_fill()
    t.lt(45)
    t.forward(tamanho) ## Pode colocar t.fd() que funciona igual
    t.rt(90)
    t.forward(tamanho) ## Pode colocar t.fd() que funciona igual
    t.end_fill()


#### Desenhar uma ESPIRAL
def espiral(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    color= textinput("COR","Digite a cor desejada:")
    t.color(color)
    t.begin_fill()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.lt(90)
        t.forward(tamanho) ## Pode colocar t.fd() que funciona igual
    t.end_fill()
## Desenhar um Hexagono
def hexagono(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    color= textinput("COR","Digite a cor desejada:")
    t.color(color)
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(8):
        t.forward(tamanho) ## Pode colocar t.fd() que funciona igual
        t.lt(45)
    t.end_fill()

## Desenhar um Quadrado

def quadrado(x,y,tamanho,color):
    t.lt(45)
    t.pu()
    t.goto(x,y)
    t.pd()
    color= textinput("COR","Digite a cor desejada:")
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.fd(tamanho)
    t.rt(90)
    t.fd(50)
    t.fd(tamanho)
    t.rt(90)
    t.fd(70)
    t.end_fill()



## CHAMADAS
cartesiano()
x = randint (50,100)
y = randint (50,100)
triangulo(x,y,90,"green")
x = randint (100,250)
y = randint (-250,-50)
espiral(x,y,60,"pink")
x = randint (-250,-50)
y = randint (-250,-50)
hexagono(x,y,90,"blue")
x = randint (-250,-50)
y = randint (50,250)
quadrado(x,y,90,"black")

mainloop()
