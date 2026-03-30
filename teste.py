import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_star(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_flag():
    # Configuração da tela
    turtle.setup(600, 400)
    turtle.speed(3)
    
    # Cores (Azul e Vermelho)
    blue = "#002A8F" # [7] Ficheiro:Flag of Cuba.svg – Wikipédia, a enciclopédia livre
    red = "#DA291C"
    
    # 5 Faixas (3 azul, 2 brancas)
    stripe_height = 400 / 5
    draw_rectangle(blue, -300, 200, 600, stripe_height)
    draw_rectangle("white", -300, 200 - stripe_height, 600, stripe_height)
    draw_rectangle(blue, -300, 200 - 2 * stripe_height, 600, stripe_height)
    draw_rectangle("white", -300, 200 - 3 * stripe_height, 600, stripe_height)
    draw_rectangle(blue, -300, 200 - 4 * stripe_height, 600, stripe_height)
    
    # Triângulo Vermelho
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.color(red)
    turtle.begin_fill()
    turtle.goto(-100, 0)
    turtle.goto(-300, -200)
    turtle.goto(-300, 200)
    turtle.end_fill()
    
    # Estrela Branca
    draw_star("white", -220, 25, 60)
    
    turtle.hideturtle()
    turtle.done()

# draw_flag()
turtle.mainloop()