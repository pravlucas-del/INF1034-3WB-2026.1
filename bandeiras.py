from turtle import *
from time import sleep
import turtle 

screen = turtle.Screen()
screen.title("Bandeira Costa Rica")
screen.setup(width=600, height=400)
t=turtle.Turtle()
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
turtle.done()
t.speed(5)
t.clear()

# Chile

for _ in range(4):
    t.forward(100)
    t.right(90)
    

largura=300
altura=200
def desenhar_retangulo(cor,x,y,l,a):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(cor)
    t.begin_fill()
    for _ in range(2):
        t.forward(1)
        t.right(90)
        t.forward(a)
        t.right(90)
    t.end_fill()




mainloop()
