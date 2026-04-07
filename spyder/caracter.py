import math

def monta_linha():
    linha = '+' * 5
    return linha

def monta_fração(numerador, denominador):
    linha = monta_linha()
    string = f"{numerador}\n{linha}\n{denominador}"
    return string

def exibe_respota(fração1, fração2,resposta):
    linha = monta_linha(10)
    print(linha)
    print(f"{fração1} + {fração2} = {resposta}")
    print(linha)

def main():
    num1 = int(input("Digite o numerador da primeira fração: "))
    den1 = int(input("Digite o denominador da primeira fração: "))
    num2 = int(input("Digite o numerador da segunda fração: "))
    den2 = int(input("Digite o denominador da segunda fração: "))
    
    fração1 = monta_fração(num1, den1)
    fração2 = monta_fração(num2, den2)
    
    exibe_respota(fração1, fração2) 

main()

