# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:11:41 2026

@author: G2612066
"""

nome="Lucas"
idade= 22
altura=1.70
print(nome,idade,altura)

# Saída formatada usando Interpolação
s= "O aluno %s tem %d anos e %.2f de altura" %(nome,idade,altura)
print(s)

# Saída formatada usando fstring
nome="Lucas"
idade= 22
altura=1.70
print(nome,idade,altura)


print(f" O Aluno {nome} tem {idade} anos e {altura:.1f} de altura")

# Escreva um programa que leia nome e 
# ultimo  nome do usuario do teclado e exiba o 
# nome completo e o nome no formato ult,nome (ex anteior)

nome=input("Qual é o seu nome?")
ultnome=input("Qual é o seu  ultimo nome?")
nc= nome+' '+ ultnome
print(nc)

idade=int(input("Qual a sua idade?"))
print(idade+1)
print(type(idade))

altura=float(input("Qual a sua altura?"))
print(altura)

