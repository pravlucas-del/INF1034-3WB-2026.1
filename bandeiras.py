from turtle import *
from time import sleep
import turtle

# ========== CONFIGURAÇÃO GLOBAL ========== 
screen = turtle.Screen()

t = turtle.Turtle()
t.hideturtle()



# Bandeira Brasil 25xp
def desenhar_Brasil():
    screen.title("Bandeira do Brasil")
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
    screen.title("Bandeira Japão")
    t.speed(5)
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

# Bandeira Bahamas 50xp

# Desenhar Retângulos
def des_ret(color, width, height, x, y):
    screen.title("Bandeira Bahamas")
    t.speed(5)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Desenhar Triângulos
def des_trian(color,x1,y1,x2,y2,x3,y3):
    t.pu()
    t.goto(x1,y1)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x1,y1)
    t.end_fill()

# Bandeira Holanda 25xp
def desen_holanda():
    screen.title("Bandeira Holanda")
    t.speed(5)
    des_ret('#21468B', 400, 80, -200, 120)
    des_ret('white', 400, 80, -200, 40)
    des_ret('#AE1C28', 400, 80, -200, -40)
sleep(5)
t.clear()

    
# Bandeira Reino Unido 75xp
def desenhar_retangulo(cor, largura, altura, x, y):
    screen.title("Bandeira Reino Unido")
    t.speed(5)
    t.pu()
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(largura)
        t.left(90)
        t.forward(altura)
        t.left(90)
    t.end_fill()

def desenhar_diagonal(cor, espessura, x1, y1, x2, y2):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.color(cor)
    t.pensize(espessura)
    t.goto(x2, y2)

# Fundo azul
desenhar_retangulo("#012169", 600, 300, -300, -150)
# 2. Cruzes Diagonais 
desenhar_diagonal("white", 40, -300, 150, 300, -150)
desenhar_diagonal("white", 40, -300, -150, 300, 150)
desenhar_diagonal("#C8102E", 15, -300, 150, 300, -150)
desenhar_diagonal("#C8102E", 15, -300, -150, 300, 150)
# 3. Cruz Central Branca 
desenhar_retangulo("white", 600, 100, -300, -50)
desenhar_retangulo("white", 100, 300, -50, -150)
# 4. Cruz Central Vermelha
desenhar_retangulo("#C8102E", 600, 60, -300, -30)
desenhar_retangulo("#C8102E", 60, 300, -30, -150)
t.hideturtle()

# Bandeira Africa do Sul 75xp
def bandeira_africa():
    screen.title("Bandeira Africa do Sul")
    retangulo_afr(-450, 300, 900, 200, '#e03c31')
    retangulo_afr(-450, 100, 900, 200, '#ffffff')
    retangulo_afr(-450, -100, 900, 200, '#001489')
    retangulo_afr(-450, 300, 112.5, 600, '#ffffff')
    triangulo_afr(-337.5, 300, 600, '#ffffff')
    retangulo_afr(-450, 60, 900, 120, '#007749')
    retangulo_afr(-450, 300, 50, 600, '#007749')
    triangulo_afr(-400, 300, 600, '#007749')
    triangulo_afr(-450, 235, 470, '#ffb81c')
    triangulo_afr(-450, 202.5, 405, '#000000')
    base_afr()

def retangulo_afr(x, y, fd_x, fd_y, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.fd(fd_x)
        t.rt(90)
        t.fd(fd_y)
        t.rt(90)
    t.end_fill()


def triangulo_afr(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.rt(30)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.end_fill()
    t.setheading(0)

def base_afr():
    t.pu()
    t.color('black')
    t.goto(-450, 300)
    t.pd()
    for _ in range(2):
        t.fd(900)
        t.rt(90)
        t.fd(600)
        t.rt(90)

# Bandeira Grécia 75xp
def grecia():
    screen.title("Bandeira Grécia")
    for i in range(8):
        if (i % 2 == 0):
            color = '#0d5eaf'
        else:
            color = '#ffffff'
        retangulo_afr(-450, 300-(i*66), 900, 66, color)
    color = '#0d5eaf'
    retangulo_afr(-450, -228, 900, 72, color)
    retangulo_afr(-450, 300, 320, 320, color)
    t.color('#ffffff')
    t.pu()
    t.goto(-323, 300)
    t.pd()
    t.begin_fill()
    for _ in range(2):
        t.fd(66)
        t.rt(90)
        t.fd(132)
        t.lt(90)
        t.fd(127)
        t.rt(90)
        t.fd(66)
        t.rt(90)
        t.fd(127)
        t.lt(90)
        t.fd(132)
        t.rt(90)
    t.end_fill()
    base_afr()

# Bandeira República Centro-Africana 75xp
def centr_afr():
    screen.title("Bandeira República Centro-Africana")
    retangulo_afr(-450, 300, 900, 150, '#003082')
    retangulo_afr(-450, 150, 900, 150, '#ffffff')
    retangulo_afr(-450, 0, 900, 150, '#289728')
    retangulo_afr(-450, -150, 900, 150, '#ffce00')
    retangulo_afr(-75, 300, 150, 600, '#d21034')
    estrela_afr(-350, 240, 50, '#ffce00')
    base_afr()

def estrela_afr(x, y, size, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(72)
    t.end_fill()

# Bandeira Islândia 50xp
screen.title("Bandeira da Islândia")

t.speed(5) 

# Função para desenhar retângulos preenchidos
def draw_rect(color, x, y, width, height):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# 1. Fundo Azul
draw_rect("#004899", -360, 250, 720, 500)

# 2. Cruz Branca
draw_rect("#FFFFFF", -360, 60, 720, 120)
draw_rect("#FFFFFF", -100, 250, 120, 500)

# 3. Cruz Vermelha 
draw_rect("#DC1E35", -360, 30, 720, 60)
draw_rect("#DC1E35", -70, 250, 60, 500)

t.hideturtle()

sleep(5)
t.clear()    
mainloop()