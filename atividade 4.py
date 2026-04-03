from turtle import *

from math import sqrt

from time import sleep

import random
import turtle

t = Turtle()

t.speed(0)


# - y = √x (50XP)
def raiz(x):
    y = sqrt(x)
    return y
 # - y = 1/x (50XP)
def divisão(x):
    y = 1/x
    if x== 0:
        x = 1
    return y
 # - y = 2^x (50XP)
def potência(x):
    y = 2**x
    return y
# - y = 5 - x^2 (75XP)
def equa(x):
    y = 5 - (x**2)
    return y
# - y = x^2 - 5x + 6 (75XP)
def equa2(x):
    y = (x**2) - (5*x) + 6
    return y
# - y = x^3 - x^2 - x + 1 (75XP)
def equa3(x):
    y = (x**3) - (x**2) - x + 1
    return y


def bp():
    plano_cartesiano()
    t.pu()
    x = 0
    y = raiz(x)
    t.goto(x, y)
    t.pd()
    t.color('red')
    for x in range(1,100):
        y = raiz(x)
        t.goto(x, y)

t.clear()

def div():
    plano_cartesiano()
    t.color('green')
    # Lado Esquerdo
    t.pu()
    x = -300
    y = divisão(x/50) * 10
    t.goto(x,y)
    t.pd()
    for x in range(-299,0):
        y = divisão(x/50) * 10
        t.goto(x,y)
    #Lado Direito
    t.pu()
    x = 1 
    y = divisão(x/50) * 10
    t.goto(x,y)
    t.pd()
    for x in range(2,301):
        y = divisão(x/50) * 10
        t.goto(x,y)

    
t.clear()

def pot():
    plano_cartesiano()
    t.pu()
    x = -100
    y = potência(x)
    t.goto(x, y)
    t.pd()
    t.color('blue')
    for x in range(-99,101):
        y = potência(x)
        t.goto(x*3, y*3)
t.clear()

def eq1():
    plano_cartesiano()
    t.pu()
    x = -100
    y = equa(x)
    t.goto(x, y)
    t.pd()
    t.color('green')
    for x in range(-99,101):
        y = equa(x)
        t.goto(x*3, y*3)
t.clear()

def eq2():
    plano_cartesiano()
    t.pu()
    x = -100
    y = equa2(x)
    t.goto(x, y)
    t.pd()
    t.color('purple')
    for x in range(-99,101):
        y = equa2(x)
        t.goto(x*3, y*3)
t.clear()

def eq3():
    plano_cartesiano()
    t.pu()
    x = -100
    y = equa3(x)
    t.goto(x, y)
    t.pd()
    t.color('red')
    for x in range(-99,101):
        y = equa3(x)
        t.goto(x*3, y*3)
    sleep(3)
    t.clear()


# Plano Cartesiano
# Eixo X
def plano_cartesiano():
    t.setheading(0)
    t.color('black')
    t.pu()
    t.goto(-300,0)
    t.pd()
    t.goto(300,0)
    t.stamp()
    # Eixo Y
    t.pu()
    t.goto(0,-300)
    t.pd()
    t.goto(0,300)
    t.lt(90)
    t.stamp()
   
def correr_tartaruga(n):
    #Configuração da tela
    screen = turtle.Screen()
    screen.title("Corrida de {n} Tartarugas")
    screen.setup(width=800, height=600)

    #Linha de chegada
    finish_line = 350

    #Criar as N tartarugas
    tartarugas = []
    cores = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'cyan']

    # Espaçamento vertical entre as tartarugas
    y_pos = -(n * 20) // 2
    for i in range(n):
        t = turtle.Turtle(shape="turtle")
        t.penup()
        # Define cor (cicla cores se N > len(cores))
        t.color(cores[i % len(cores)])
        t.goto(-280, y_pos)
        tartarugas.append(t)
        y_pos += 40
    # Lógica da corrida
    corrida = True
    while corrida:
        for t in tartarugas:
            distancia = random.randint(1, 10)
            t.forward(distancia)

            # Checar Vencedor
            if t.xcor() >= finish_line:
                vencedor = t.color()[0]
                print(f"A tartaruga {vencedor} venceu!")
                corrida = False
                break
    



    




bp()
sleep(3)
t.clear()
div()
sleep(3)
t.clear()
pot()
sleep(3)
t.clear()
eq1()
sleep(3)
t.clear()
eq2()
sleep(3)
t.clear()
eq3()
sleep(3)
t.clear()
correr_tartaruga(5)





mainloop()