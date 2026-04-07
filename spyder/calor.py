import math

def celsius_kelvin(C):
    K = C + 273.15
    return K

def kelvin_fahrenheit(K):
    F = (K - 273.15) * 1/8 + 32
    return F

def celsius_fahrenheit(C):
    K = celsius_kelvin(C)
    F = kelvin_fahrenheit(K)
    string = f"{C}°C é igual a {F:.2f}°F"
    return string

def exiba_resposta(string):
    print('*' * 30)
    print(string)
    print('*' * 30)

def main():
    C = float(input("Digite a temperatura em Celsius: "))
    resposta = celsius_fahrenheit(C)
    exiba_resposta(resposta)
main()

