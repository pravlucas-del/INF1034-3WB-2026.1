import math

def calcula_volume_cilindro(raio, altura):
    volume = math.pi * (raio ** 2) * altura
    return volume

def calcula_volume_cone(raio, altura):
    volume = calcula_volume_cilindro(raio, altura) / 3
    return volume

def exibe_diferença_volumes(volume_cilindro, volume_cone):
    diferença = volume_cilindro - volume_cone
    print(f"A diferença entre o volume do cilindro e do cone é: {diferença:.2f}")

def main():
    raio = float(input("Digite o raio da base do cilindro e cone: "))
    altura = float(input("Digite a altura do cilindro e cone: "))
    volume_cilindro = calcula_volume_cilindro(raio, altura)
    volume_cone = calcula_volume_cone(raio, altura)
    exibe_diferença_volumes(volume_cilindro, volume_cone)

main()