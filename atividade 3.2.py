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

def retangulo(x,y,alt,larg,color):
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

 


def desenhar_brasil():

    screen.title("Bandeira do Brasil")
    t.speed(5)
    desenhar_retangulo(-200,120,240,400,'green')
    desenhar_Losango(0,100,'yellow',180,0,0,-100,0,100,-180,0,0,-100)
    circulo(0,-70,'blue')

    

sleep(3)
t.clear()

def desenha_japão():
    desenhar_retangulo(-200,120,240,400,'white')
    circulo(0,-70,'red')

sleep(3)
t.clear()
def desen_holanda():
    retangulo(-200, 120, 400, 80, '#21468B')
    retangulo(-200, 40, 400, 80, 'white')
    retangulo(-200, -40, 400, 80, '#AE1C28')
sleep(5)
t.clear()

def desen_Italia():
    retangulo(-200, 120, 133.33, 240, '#009246')
    retangulo(-66.67, 120, 133.33, 240, 'white')
    retangulo(66.67, 120, 133.33, 240, '#CE2B37')

def desen_França():
    retangulo(-200, 120, 133.33, 240, '#0055A4')
    retangulo(-66.67, 120, 133.33, 240, 'white')
    retangulo(66.67, 120, 133.33, 240, '#CE2B37')

def desen_Alemanha():
    retangulo(-200, 120, 400, 80, '#000000')
    retangulo(-200, 40, 400, 80, '#DD0000')
    retangulo(-200, -40, 400, 80, '#FFCE00')

def desen_Iêmen():
    
    retangulo(-200, 120, 400, 80, '#CE1126')
    retangulo(-200, 40, 400, 80, '#FFFFFF')
    retangulo(-200, -40, 400, 80, '#000000')
    

def desen_Belgica():
    retangulo(-200, 120, 133.33, 240, '#000000')
    retangulo(-66.67, 120, 133.33, 240, '#FAE042')
    retangulo(66.67, 120, 133.33, 240, '#EF2B2D')

def desen_Romaneia():
    retangulo(-200, 120, 133.33, 240, '#002B7F')
    retangulo(-66.67, 120, 133.33, 240, '#FCD116')
    retangulo(66.67, 120, 133.33, 240, '#CE1126')

def desen_Irlanda():
    retangulo(-200, 120, 400, 80, '#009A4B')
    retangulo(-200, 40, 400, 80, '#FFFFFF')
    retangulo(-200, -40, 400, 80, '#FF883E')

def desen_Hungria():
    retangulo(-200, 120, 400, 80, '#CD2A3E')
    retangulo(-200, 40, 400, 80, '#FFFFFF')
    retangulo(-200, -40, 400, 80, '#00664B')

def desen_Austria():
    retangulo(-200, 120, 400, 80, '#FF0000')
    retangulo(-200, 40, 400, 80, '#FFFFFF')
    retangulo(-200, -40, 400, 80, '#FF0000')

def desen_Bolivia():
    retangulo(-200, 120, 400, 80, '#D52B1E')
    retangulo(-200, 40, 400, 80, '#FFD100')
    retangulo(-200, -40, 400, 80, '#007A5E')

def desen_Ucrania():
        retangulo(-200, 120, 400, 80, '#0057B7')
        retangulo(-200, 40, 400, 80, '#FFD100')


def desen_Armenia():
    retangulo(-200, 120, 400, 80, '#D90012')
    retangulo(-200, 40, 400, 80, '#0057B7')
    retangulo(-200, -40, 400, 80, '#FFEF00')


def desen_Monaco():
    retangulo(-200, 120, 400, 80, '#E31B23')
    retangulo(-200, 40, 400, 80, '#FFFFFF')
    

def desen_Nigeria():
    retangulo(-200, 120, 133.33, 240, '#008753')
    retangulo(-66.67, 120, 133.33, 240, 'white')
    retangulo(66.67, 120, 133.33, 240, '#008753')

def desen_Costa_do_Marfin():
    retangulo(-200, 120, 133.33, 240, '#FF8B00')
    retangulo(-66.67, 120, 133.33, 240, '#FFFFFF')
    retangulo(66.67, 120, 133.33, 240, '#009E60')

def desen_Colombia():
    retangulo(-200, 120, 400, 80, '#FFD100')
    retangulo(-200, 40, 400, 80, '#003893')
    retangulo(-200, -40, 400, 80, '#CE1126')

def desen_Lituania():
    retangulo(-200, 120, 400, 80, '#FDB913')
    retangulo(-200, 40, 400, 80, '#006A44')
    retangulo(-200, -40, 400, 80, '#C1272D')


ddesenhar_Brasil()
desen_japão()
sleep(3)
t.clear()
desen_holanda()
sleep(3)
t.clear()
desen_Italia()
sleep(3)
t.clear()
desen_França()
sleep(3)
t.clear()
desen_Alemanha()
sleep(3)
t.clear()
desen_Iêmen()
sleep(3)
t.clear()
desen_Belgica()
sleep(3)
t.clear()
desen_Romaneia()
sleep(3)
t.clear()
desen_Irlanda()
sleep(3)
t.clear()
desen_Hungria()
sleep(3)
t.clear()
desen_Austria()
sleep(3)
t.clear()
desen_Bolivia()
sleep(3)
t.clear()
desen_Ucrania()
sleep(3)
t.clear()
desen_Armenia()
sleep(3)
t.clear()
desen_Monaco()
sleep(3)
t.clear()
desen_Nigeria()
sleep(3)
t.clear()
desen_Costa_do_Marfin()
sleep(3)
t.clear()
desen_Colombia()
sleep(3)
t.clear()
desen_Lituania()
sleep(3)
t.clear()

mainloop()