from turtle import *
from time import sleep
import turtle


t = Turtle()
def retangulo(x, y, largura, altura, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.fd(largura)
        t.rt(90)
        t.fd(altura)
        t.rt(90)
        
    t.end_fill()


def desenhar_Brasil():
    
    t.speed(5)
    # Retangulo verde
    t.pu()
    t.goto(-200,120)
    t.pd()
    t.color("#009440")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(240)
        t.right(90)
    t.end_fill()

    # Losangolo Amarelo
    t.pu()
    t.goto(0,100)
    t.pd()
    t.color('#ffcb00')
    t.begin_fill()
    t.goto(180,0)
    t.goto(0,-100)
    t.goto(-180,0)
    t.goto(0,100)
    t.end_fill()

    # Circulo Azul
    t.pu()
    t.goto(0,-70)
    t.setheading(0)
    t.pd()
    t.color('#002776')
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    t.hideturtle()
    
t.clear()

# Bandeira Japão 25xp
def desen_japão():
    
    
    
    # Retangulo Branco
    t.pu()
    t.goto(-200,120)
    t.pd()
    t.color('#FFFFFF')
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(240)
        t.right(90)
    t.end_fill()
    # Círculo Vermelho
    t.pu()
    t.goto(0,-70)
    t.setheading(0)
    t.pd()
    t.color('#BC002D')
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    t.hideturtle()
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





desenhar_Brasil()
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
