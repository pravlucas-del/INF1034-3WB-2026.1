import math

# a) Função para calcular o lado entre dois vértices
def calcula_lado(p1, p2):
    
    x1, y1 = p1
    x2, y2 = p2
    # Fórmula da distância: sqrt((x2-x1)^2 + (y2-y1)^2)
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# b) Função para calcular o perímetro (soma dos lados)
def calcula_perimetro(p1, p2, p3):
    """
    Calcula o perímetro do triângulo formado pelos vértices p1, p2 e p3.
    """
    # Chama a função calcula_lado para cada par de vértices
    lado1 = calcula_lado(p1, p2)
    lado2 = calcula_lado(p2, p3)
    lado3 = calcula_lado(p3, p1)
    
    perimetro = lado1 + lado2 + lado3
    return perimetro

# Bloco Principal
def main():
    print("Digite as coordenadas (x, y) dos 3 vértices do triângulo:")
    
    try:
        # Captura as coordenadas
        x1 = float(input("Vértice 1 - x: "))
        y1 = float(input("Vértice 1 - y: "))
        
        x2 = float(input("Vértice 2 - x: "))
        y2 = float(input("Vértice 2 - y: "))
        
        x3 = float(input("Vértice 3 - x: "))
        y3 = float(input("Vértice 3 - y: "))
        
        # Define os pontos como tuplas
        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (x3, y3)
        
        # Chama a função de perímetro e exibe o resultado
        perimetro = calcula_perimetro(p1, p2, p3)
        print(f"\nO perímetro do triângulo é: {perimetro:.2f}")
        
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")

main()
