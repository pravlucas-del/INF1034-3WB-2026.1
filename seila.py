import math
import random


def jogo_pipoca():
    p1=int(input("Insira a quantidade de pipoca do Pote 1 : "))
    p2=int(input("Insira a quantidade de pipoca do Pote 2 : "))
    pote=[p1, p2]
    print("Pote 1: ", pote[0])
    print("Pote 2: ", pote[1])
    print("Pote 1 e Pote 2: ", pote)
    return pote

    


def rodada1(pote1, pote2):
    print("Rodada 1")
    c1=int(input("Jogador 1, quantidade de pipoca comida do Pote 1:  "))
    c2=int(input("Jogador 2, quantidade de pipoca comida do Pote 2:  "))
   
    result1 = pote1 - c1
    result2 = pote2 - c2
    
    print("Pote 1: ", result1)
    print("Pote 2: ", result2)
    print("Pote 1 e Pote 2: ", [result1, result2])
    return result1, result2

def rodada2(result1, result2):
    print("Rodada 2")
    c3=int(input("Jogador 1, quantidade de pipoca comida do Pote 1:  "))
    c4=int(input("Jogador 2, quantidade de pipoca comida do Pote 2:  "))
   
    result3 = result1 - c3
    result4 = result2 - c4
    r = [c3, c4]
    print("Pote 1: ", result3)
    print("Pote 2: ", result4)
    print("Pote 1 e Pote 2: ", [result3, result4])
    return result3, result4

def rodada3(result3, result4):
    print("Rodada 3")
    c5=int(input("Jogador 1, quantidade de pipoca comida do Pote 1:  "))
    c6=int(input("Jogador 2, quantidade de pipoca comida do Pote 2:  "))
   
    result5 = result3 - c5
    result6 = result4 - c6
    r = [c5, c6]
    print("Pote 1: ", result5)
    print("Pote 2: ", result6)
    print("Pote 1 e Pote 2: ", [result5, result6])
    return result5, result6

def vencedor(result5, result6):
    print("Vencedor: ")
    result7 = result5 > result6
    result8 = result5 < result6
    print("Jogador 1: ", result7)
    print("Jogador 2: ", result8)
    print("Jogador 1 e Jogador 2: ", [result7, result8])
    true = "Jogador 1"
    false = "Jogador 2"
    final = [true, false]

    



potes =jogo_pipoca()
result1, result2 = rodada1(potes[0], potes[1])
result3, result4 = rodada2(result1, result2)
result5, result6 = rodada3(result3, result4)
vencedor(result5, result6)