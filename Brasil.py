# a) Função converteAlqueirePaulistaEmM2
def converteAlqueirePaulistaEmM2(alqueires):
    
    return alqueires * 24200.0

# b) Função converteAlqueireDoNorteEmM2
def converteAlqueireDoNorteEmM2(alqueires):
    
    return alqueires * 27225.0

# c) Função exibeTotalDeTerras
def exibeTotalDeTerras(qtd_paulista, qtd_norte):
    
    total_m2 = converteAlqueirePaulistaEmM2(qtd_paulista) + \
               converteAlqueireDoNorteEmM2(qtd_norte)
    print(f"Total de terras: {total_m2:,.2f} m2")

# d) Programa Principal
def main():
    try:
        # Leitura dos dados
        paulista = float(input("Digite a quantidade de alqueires paulistas: "))
        norte = float(input("Digite a quantidade de alqueires do norte: "))
        
        # Chamada da função de exibição
        exibeTotalDeTerras(paulista, norte)
        
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

main()
