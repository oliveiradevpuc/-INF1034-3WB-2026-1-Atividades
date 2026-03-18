from turtle import *

t = Turtle()

## PLANO CARTESIANO 
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

## POSICAO DA SETA
t.lt(90)

## TRIANGULO 
t.pu()
t.goto(-200,100)
t.pd()
color= textinput("COR","Digite a cor desejada:")
t.color("black")
t.begin_fill()
t.fillcolor(color)
t.begin_fill()
t.lt(45)
t.forward(100) ## Pode colocar t.fd() que funciona igual
t.rt(90)
t.forward(100) ## Pode colocar t.fd() que funciona igual
t.end_fill()

## espiral
t.pu()
t.goto(200,100)
t.pd()
color= textinput("COR","Digite a cor desejada:")
t.color("black")
t.begin_fill()
t.fillcolor(color)
t.begin_fill()
for _ in range(4):
    t.lt(90)
    t.forward(100) ## Pode colocar t.fd() que funciona igual
t.end_fill()

# HEXAGONO
t.pu()
t.goto(-200,-200)
t.pd()
color= textinput("COR","Digite a cor desejada:")
t.color("black")
t.begin_fill()
t.fillcolor(color)
for _ in range(8):
    t.forward(50) ## Pode colocar t.fd() que funciona igual
    t.lt(45)
t.end_fill()

## ESPIRAL + RETANGULO

t.pu()
t.goto (120,-200)
t.pd()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(100)
t.pu()
t.goto (200,-200)
t.pd()
t.forward(_)
for _ in range(45):
    t.forward(_)
    t.left(59)


mainloop()
