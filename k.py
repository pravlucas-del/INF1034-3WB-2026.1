from turtle import *
from random import randint


t = Turtle()
# Começo do plano cartesiano
def plano_cartesiano():
    t.goto(-300,0)
    t.pu()
    t.goto(0,0)
    t.pd()
    t.goto(300,0)
    t.stamp()
    t.pd()
    t.goto(0,0)
    t.pd()
    t.goto(0,-300)
    t.pd()
    t.goto(0,300)
    t.pd()
    t.left(90)
    t.stamp()
    t.rt(90)
plano_cartesiano()

def desenha_quadrado(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.fd(tamanho)
        t.right(90)
    t.end_fill()


x = randint(200,300)
y = randint(100,200)
desenha_quadrado(x,y,100,'blue')


def de_pentagono(x,y,tamnaho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(12):
        t.fd(tamnaho)
        t.right(30)
    t.end_fill()

x= randint(-200,-100)
y= randint(200,300)
de_pentagono(x,y,50,'purple')

def desenhar_poligono(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(8):
        t.fd(tamanho)
        t.right(45)
    t.end_fill()

desenhar_poligono(-200,-100,50,'grey')

def des_triangulo(x,y,tamanho,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.fd(tamanho)
        t.lt(120)
    t.end_fill()

x = randint(100,300)
y = randint(-300,-0 )

des_triangulo(x,y,100,'black')

#Spiral farm aura
color = textinput("Obter cor", "Digite a cor:")
t.color("black")
t.begin_fill()
t.fillcolor( color)
t.pu()
t.goto(150,-100)
t.pd()
t.speed(0)
for i in range(40):
    t.fd(i*2)
    t.lt(45)





mainloop()
