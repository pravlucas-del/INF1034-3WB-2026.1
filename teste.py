import turtle
import random

def correr_tartarugas(n):
    # Configuração da tela
    screen = turtle.Screen()
    screen.title(f"Corrida de {n} Tartarugas")
    screen.setup(width=600, height=400)
    
    # Linha de chegada
    finish_line = 250
    
    # Criar as N tartarugas
    tartarugas = []
    cores = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "brown"]
    
    # Espaçamento vertical entre tartarugas
    y_pos = - (n * 20) // 2
    
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
            
            # Checar vencedor
            if t.xcor() >= finish_line:
                vencedor = t.color()[0]
                print(f"A tartaruga {vencedor} venceu!")
                corrida = False
                break
                
    screen.exitonclick()

# Exemplo de uso: correr_tartarugas(5)
correr_tartarugas(5)
mainloop()