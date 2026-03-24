from turtle import *
from time import sleep
import turtle

# ========== CONFIGURAÇÃO GLOBAL ========== 
screen = turtle.Screen()

t.Turtle()
t.hideturtle()



# Bandeira Brasil 25xp
def desenhar_bandeira():
    screen.title("Bandeira do Brasil")
    t.speed(5)
    # Retangulo verde
    t.pu()
    t.goto(-200,120)
    t.pd()
    t.color("#009440)
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
    t.hiderturtle()
    t.clear()
desenhar_bandeira()

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
    # Círculo Vermelho
    t.pu()
    t.goto(0,-70)
    t.setheading(0)
    t.pd()
    t.color('#BC002D')
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    t.hiderturtle()
    t.clear()
desen_japão()

# Bandeira Bahamas 50xp

# Desenhar Retângulos
def des_ret(color,widght,height,x,y):
    screen.title("Bandeira Bahamas")
    t.speed(5)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(widght)
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

# Desenhar Faixas 
des_ret("#00778B",800,500,-400,250)
des_ret('#F9DD15',800,167,-400,-83)

# Desenhar Faixa Central
des_ret("#FFC72C",800,166,-400,83)

# Desenhar Triângulo Preto
t.pu()
t.goto(-400,250)
t.pd()
t.color("black")
t.begin_fill()
t.goto(0,0)
t.goto(-400,-250)
t.goto(-400,250)
t.end_fill()
t.hiderturtle()
t.clear()

# Bandeira Chile 50xp
def d_reta(t,cor,largura,altura):
    screen.title("Bandeira Chile")
    t.speed(5)
    t.begin_fill()
    t.fillcolor(cor)
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

def desenhar_estrela(t,tamanho):
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)
    t.end_fill()

# Faixa Vermelha
t.pu()
t.goto(-150,-100)
t.pd()
d_reta(t,"#D52B1E",largura,100)

# Faixa Branca
t.pu()
t.goto(-150,0)
t.pd()
d_reta(t,"white",largura,100)

# Quadrado azul
t.pu()
t.goto(-150,100)
t.pd()
d_reta(t,"#0039A6",100,100)

# Estrela
t.pu()
t.goto(-100,65)
t.pd()
desenhar_estrela(t,40)
t.hiderturtler()
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
t.hiderturtle()
t.clear()

# Bandeira Africa do Sul 75xp

def bandeira():
    screen.title("Bandeira Africa do Sul")
    retangulo(-450, 300, 900, 200, '#e03c31')
    retangulo(-450, 100, 900, 200, '#ffffff')
    retangulo(-450, -100, 900, 200, '#001489')
    retangulo(-450, 300, 112.5, 600, '#ffffff')
    triangulo(-337.5, 300, 600, '#ffffff')
    retangulo(-450, 60, 900, 120, '#007749')
    retangulo(-450, 300, 50, 600, '#007749')
    triangulo(-400, 300, 600, '#007749')
    triangulo(-450, 235, 470, '#ffb81c')
    triangulo(-450, 202.5, 405, '#000000')
    base()
def retangulo(x, y, fd_x, fd_y, color):
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
def triangulo(x, y, size, color):
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
    
def base():
    t.pu()
    t.color('black')
    t.goto(-450, 300)
    t.pd()
    for _ in range(2):
        t.fd(900)
        t.rt(90)
        t.fd(600)
        t.rt(90)
        t.clear()
 # Bandeira Grécia 75xp
def grecia():
    for i in range(8):
        if (i % 2 == 0):
            color = '#0d5eaf'
        else:
            color = '#ffffff'
        retangulo(-450, 300-(i*66), 900, 66, color)
    color = '#0d5eaf'
    retangulo(-450, -228, 900, 72, color)
    retangulo(-450, 300, 320, 320, color)
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
    t.clear
    base()

#  Bandeira República Centro-Africana 75xp
def centr_afr():
    retangulo(-450, 300, 900, 150, '#003082')
    retangulo(-450, 150, 900, 150, '#ffffff')
    retangulo(-450, 0, 900, 150, '#289728')
    retangulo(-450, -150, 900, 150, '#ffce00')
    retangulo(-75, 300, 150, 600, '#d21034')
    estrela(-350, 240, 50, '#ffce00')
    t.clear()
    base()

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
draw_rect( "#DC1E35", -360, 30, 720, 60)
draw_rect( "#DC1E35", -70, 250, 60, 500)


t.hideturtle()

sleep(5)
t.clear()    
mainloop()    
