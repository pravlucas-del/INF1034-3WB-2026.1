from turtle import *

t=Turtle
from turtle import *
from time import sleep
import turtle

# ========== CONFIGURAÇÃO GLOBAL ========== 
screen = turtle.Screen()

t = turtle.Turtle()
t.hideturtle()



# Desenhar Retângulos

def desenhar_retangulo(x,y,alt,larg,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()

def circulo(x,y,color):
    t.pu()
    t.goto(x,y)
    
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(70)
    t.end_fill()
    t.hideturtle()

def desenhar_Losango(x1,y1,color,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6):
    t.pu()
    t.goto(x1,y1)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x5,y5)
    t.goto(x6,y6)
    t.end_fill()

def desenhar_triangulo(x,y,color,x2,y2,x3,y3):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.goto(x2,y2)
    t.goto(x3,y3)
    
    
    
        
    t.end_fill()
   
def desenhar_diagonal(cor, espessura, x1, y1, x2, y2):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.color(cor)
    t.pensize(espessura)
    t.goto(x2, y2)   


def desenhar_brasil():

    screen.title("Bandeira do Brasil")
    t.speed(5)
    desenhar_retangulo(-200,120,240,400,'green')
    desenhar_Losango(0,100,'yellow',180,0,0,-100,0,100,-180,0,0,-100)
    circulo(0,-70,'blue')

    
desenhar_brasil()
t.clear()

def desenha_japão():
    desenhar_retangulo(-200,120,240,400,'white')
    circulo(0,-70,'red')


desenha_japão()
t.clear()

def desenhar_Bahamas():
    desenhar_retangulo(-200,120,240,400,'#00778b')
    desenhar_retangulo(-200,50,100,400,'#ffc72c')
    desenhar_triangulo(-200,0,'black',180,0,100,-100)

desenhar_Bahamas()
t.clear()
def desenhar_Reino_Unido():
    desenhar_retangulo(600,300,-300,-150,'#00247D')
    desenhar_diagonal('white',40,-300,150,300,-150)
    desenhar_diagonal('white',40,-300,-150,300,150)
    desenhar_diagonal('#c8102e',15,-300,150,300,150)
    desenhar_diagonal('#c8102e',15,-300,-150,300,150)
    #Cruz central
    desenhar_retangulo(600,300,-300,-150,'white')




sleep
mainloop()