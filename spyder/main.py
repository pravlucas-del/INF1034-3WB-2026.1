
import math

def calculaRaioEsferaIncrita(V_cubo):
    raio = V_cubo ** (1/3) / 2
    return raio

def calculaVolumeEsfera(raio):
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

def main():
    V_cubo = float(input("Digite o volume do cubo: "))
    raio = calculaRaioEsferaIncrita(V_cubo)
    volume_esfera = calculaVolumeEsfera(raio)
    print(f"O raio da esfera inscrita é: {raio:.2f}")
    print(f"O volume da esfera inscrita é: {volume_esfera:.2f}")

main()

