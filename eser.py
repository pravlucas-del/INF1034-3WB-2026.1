
def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classifica_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
def main():
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcula_imc(peso, altura)
    classificação = classifica_imc(imc)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificação}")

main()