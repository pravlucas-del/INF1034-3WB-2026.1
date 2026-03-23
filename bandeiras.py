from turtle import *
from time import sleep
import turtle 

# Bandeira Costa Rica 50xp 1

screen = turtle.Screen()
screen.title("Bandeira Costa Rica")
screen.setup(width=600, height=400)
t= Turtle()
t.speed(5)
t.hideturtle()
altura_total=200
largura_total=300
largura_faixa= altura_total / 6

def desenhar_faixa(cor,y):
    t.pu()
    t.goto(-largura_total/2,y)
    t.pd()
    t.color(cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(largura_total)
        t.right(90)
        t.forward(largura_faixa)
        t.right(90)
    t.end_fill()
desenhar_faixa("#0034a3",100)
desenhar_faixa("white",100 - largura_faixa)
desenhar_faixa("#dc202c", 100-2 * largura_faixa)

desenhar_faixa("#dc202c",100-3*largura_faixa)
desenhar_faixa("white",100 - 4 * largura_faixa)
desenhar_faixa("#0030BF", 100 - 5 * largura_faixa)

sleep(5)
t.clear()

def principal():
    # Bandeira Holanda 25xp 
    facil(-450,300,900,200,'#ae1c28')
    facil(-450,100,900,200,'#ffffff')
    facil(-450,-100,900,200'#21468b')
    base()

    # Bandeira Brasil 25xp 

def desenhar_bandeira():
    screen.title("Bandeira do Brasil")
    t.Turtle()
    t.speed(5)

    # 1. Retângulo Verde
    t.pu()
    t.goto(-200, 120)
    t.pd()
    t.color("#009440") # Verde oficial
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(240)
        t.right(90)
    t.end_fill()

    # 2. Losango Amarelo
    t.pu()
    t.goto(0, 100) 
    t.pd()
    t.color("#ffcb00")
    t.begin_fill()
    t.goto(180, 0)   
    t.goto(0, -100)
    t.goto(-180, 0)  
    t.goto(0, 100)   
    t.end_fill()

    # 3. Círculo Azul
    t.pu()
    t.goto(0, -70)
    t.setheading(0)
    t.pd()
    t.color("#002776") 
    t.begin_fill()
    t.circle(70)
    t.end_fill()

    t.hideturtle()
    done()

desenhar_bandeira()


#Emirados Arabes 50xp 2

def draw_retangulo(color, x, y, width, height):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Configuração da tela

screen.title("Bandeira dos Emirados Árabes Unidos")
t.speed(5)

# Dimensões 
altura = 200
largura = 400
strip_largura = largura * 0.75  
red_largura = largura * 0.25    
strip_altura = altura / 3   

# 1. Faixa Vertical Vermelha 
draw_retangulo("#FF0000", -largura/2, -altura/2, red_largura, altura)

# 2. Faixa Horizontal Verde 
draw_retangulo("#00732F", -largura/2 + red_largura, altura/2 - strip_altura, strip_largura, strip_altura)

# 3. Faixa Horizontal Branca 
draw_retangulo("#FFFFFF", -largura/2 + red_largura, -strip_altura/2, strip_largura, strip_altura)

# 4. Faixa Horizontal Preta 
draw_retangulo("#000000", -largura/2 + red_largura, -altura/2, strip_largura, strip_altura)

# Bandeira Paquistão 50xp 3

def draw_flag():
    t.Turtle()
    t.speed(3)
    
    # Configurações iniciais
    largura = 600
    altura = 400
    
    # Desenhar o retângulo verde
    t.pu()
    t.goto(-largura/2, altura/2)
    t.pd()
    t.color("#004037") # Verde escuro
    t.begin_fill()
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()
    
    # Desenhar a faixa branca
    t.goto(-largura/2, altura/2)
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(largura/4) # 1/4 da largura
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()
    
    # Desenhar a Lua Crescente (Crescent)
    t.pu()
    t.goto(50, 60) # Posição aproximada
    t.color("white")
    t.begin_fill()
    t.circle(70) # Tamanho da lua
    t.end_fill()
    
    # Desenhar o círculo para "apagar" a lua (fazer o efeito crescente)
    t.pu()
    t.goto(75, 75)
    t.color("#004037") # Cor de fundo verde
    t.begin_fill()
    t.circle(70)
    t.end_fill()
    
    # Desenhar a Estrela
    t.pu()
    t.goto(100, 30)
    t.pd()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(50)
        t.right(144)
    t.end_fill()
    
    t.hideturtle()
    turtle.done()

draw_flag()

# Bandeira Turquia 50xp 4

def desenhar_bandeira():
    t.Turtle()
    t.speed(3)
    
    # Configurações iniciais
    largura = 600
    altura = 400
    screen.setup(largura, altura)
    screen.bgcolor("red") # Fundo Vermelho
    
    t.pu()
    t.goto(-100, -80) # Posição inicial da lua
    t.pd()
    t.color("white")
    
    # Desenhar a Lua Crescente (simplificado)
    t.begin_fill()
    t.circle(80) # Círculo externo
    t.end_fill()
    
    t.pu()
    t.goto(-70, -60) # Posição da lua interna
    t.pd()
    t.color("red")
    t.begin_fill()
    t.circle(60) # Círculo interno para fazer a lua
    t.end_fill()
    
    # Desenhar a Estrela
    t.pu()
    t.goto(50, 0)
    t.pd()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(80)
        t.right(144)
    t.end_fill()
    
    t.hideturtle()
    turtle.done()

desenhar_bandeira()

# Bandeira Noruega 50xp 5 

def draw_retangulo(t, color, largura, altura):
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

def draw_flag():
    screen.title("Bandeira da Noruega")
    
    t.Turtle()
    t.speed(5)
    
    # Dimensões 
    largura = 220
    altura = 160
    
    # 1. Fundo Vermelho
    t.pu()
    t.goto(-110, 80)
    t.pd()
    draw_retangulo(t, "#BA0C2F", largura, altura) # Vermelho Norueguês
    
    # 2. Cruz Branca (Horizontal e Vertical)
    
    # Horizontal Branca
    t.pu()
    t.goto(-110, 20) 
    t.pd()
    draw_retangulo(t, "white", largura, 40)
    
    # Vertical Branca
    t.pu()
    t.goto(-30, 80)
    t.pd()
    draw_retangulo(t, "white", 40, altura)
    
    # 3. Cruz Azul (Horizontal e Vertical)
    
    # Horizontal Azul
    t.pu()
    t.goto(-110, 10)
    t.pd()
    draw_retangulo(t, "#00205B", largura, 20) # Azul Norueguês
    
    # Vertical Azul
    t.pu()
    t.goto(-20, 80)
    t.pd()
    draw_retangulo(t, "#00205B", 20, altura)
    
    t.hideturtle()
    screen.exitonclick()

draw_flag()

# Bandeira Islândia 50xp 6

# Configuração da tela

screen.title("Bandeira da Islândia - Python Turtle")
screen.setup(largura=600, altura=400)

# Criar o objeto tartaruga
t.Turtle()
t.speed(3)
t.hideturtle()

# Função para desenhar retângulos
def draw_retangulo(color, largura, altura, x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

# Fundo Azul
draw_retangulo("#0048E0", 600, 400, -300, 200)

# Cruz Branca 
draw_retangulo("largura", 600, 100, -300, 50)
draw_retangulo("largura", 100, 400, -100, 200)

# Cruz Vermelha 
draw_retangulo("#D72828", 600, 50, -300, 25)
draw_retangulo("#D72828", 50, 400, -75, 200)

# Bandeira Africa do Sul 75xp

def desenhar_retangulo(t, cor, x, y, largura, altura):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(largura)
        t.left(90)
        t.forward(altura)
        t.left(90)
    t.end_fill()

def desenhar_poligono(t, cor, pontos):
    t.pu()
    t.goto(pontos[0])
    t.pd()
    t.color(cor)
    t.begin_fill()
    for pontos in pontos[1:]:
        t.goto(ponto)
    t.goto(pontos[0])
    t.end_fill()

# Configuração da tela

screen.title("Bandeira da África do Sul")
t.Turtle()
t.speed(5)

# Cores aproximadas (RGB/Hex)
VERMELHO = "#E23D28"
AZUL = "#002395"
VERDE = "#007749"
AMARELO = "#FFB81C"
PRETO = "#000000"
BRANCO = "#FFFFFF"

# 1. Fundo/Base (Vermelho em cima, Azul embaixo)
desenhar_retangulo(t, VERMELHO, -300, 0, 600, 200)
desenhar_retangulo(t, AZUL, -300, -200, 600, 200)

# 2. Faixa Branca (Base para o Y verde)
pontos_branco = [(-300, 200), (-300, -200), (0, 0), (600, 0), (600, 60) , (60, 60), (-240, 260)] 

# 3. Faixa Verde (Formato em Y)
desenhar_poligono(t, VERDE, [(-300, 100), (0, 0), (600, 0), (600, -60), (0, -60), (-300, -260), (-300, -180), (-80, 0), (-300, 180)])

# 4. Triângulo Preto e bordas Amarelas
desenhar_poligono(t, AMARELO, [(-300, 120), (-160, 0), (-300, -120)])
desenhar_poligono(t, PRETO, [(-300, 100), (-180, 0), (-300, -100)])

# Bandeira Coreia do Norte 75xp

def desenhar_retangulo(t, cor, largura, altura):
    t.begin_fill()
    t.fillcolor(cor)
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

def desenhar_estrela(t, cor, tamanho):
    t.begin_fill()
    t.fillcolor(cor)
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)
    t.end_fill()

def bandeira_coreia_do_norte():
    # Configuração inicial
 
    screen.title("Bandeira da Coreia do Norte")
    t.Turtle()
    t.speed(3)

    # Cores
    vermelho = "#ED1C27"
    azul = "#024FA2"
    branco = "#FFFFFF"
    
    # Dimensões (proporção aproximada)
    largura = 300
    altura = 200
    
    # Desenhar faixa azul superior
    t.pu()
    t.goto(-150, 100)
    t.pd()
    desenhar_retangulo(t, azul, largura, altura/3)
    
    # Desenhar faixas brancas 
    t.pu()
    t.goto(-150, 100 - altura/3)
    t.pd()
    desenhar_retangulo(t, branco, largura, 10)
    
    t.pu()
    t.goto(-150, -100 + altura/3 + 10)
    t.pd()
    desenhar_retangulo(t, branco, largura, 10)

    # Desenhar faixas vermelhas
    t.pu()
    t.goto(-150, 100 - altura/3 - 10)
    t.pd()
    desenhar_retangulo(t, vermelho, largura, altura/3 - 10)
    
    t.pu()
    t.goto(-150, -100 + altura/3)
    t.pd()
    desenhar_retangulo(t, vermelho, largura, altura/3 - 10)

    # Desenhar círculo branco
    t.pu()
    t.goto(0, -40) 
    t.pd()
    t.color(branco)
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    
    # Desenhar estrela vermelha
    t.pu()
    t.goto(-25, 5) 
    t.pd()
    t.color(vermelho)
    desenhar_estrela(t, vermelho, 50)

bandeira_coreia_do_norte()

# Bandeira Desafio (Canadá) 200xp


# Configuração da tela
screen.title("Bandeira do Canadá")
t = turtle.Turtle()
t.speed(3)

# Função para desenhar retângulos
def draw_rectangle(color, largura, altura):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(largura)
        t.right(90)
        t.forward(altura)
        t.right(90)
    t.end_fill()

# Desenhar faixas vermelhas e branca
draw_retangulo("red", 100, 300)
t.forward(100)
draw_retangulo("white", 200, 300)
t.forward(200)
draw_retangulo("red", 100, 300)

def desenhar_folha_canada():
    # Configuração inicial
    t.Turtle()
    screen.title("Folha do Canadá")
    screen.bgcolor("white")
    
    t.color("red")
    t.begin_fill()
    t.speed(3)
    t.left(90)
    
    # Desenho da folha (forma simplificada)
    t.forward(100)
    
    # Lado esquerdo
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    
    # Topo
    t.left(150)
    t.forward(40)
    t.right(150)
    t.forward(40)
    
    # Lado direito
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    
    t.right(120)
    t.forward(100)
    
    # Base/Caule
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    
    t.end_fill()
    


# Executar a função
desenhar_folha_canada()



sleep(5)
t.clear()
mainloop()
