import math

# a. Função quantasDeUmTipo: calcula o número de caixas necessárias
def quantasDeUmTipo(total_garrafas, capacidade_caixa):
    
    return math.ceil(total_garrafas / capacidade_caixa)

# b. Função custoTotalDeUmTipo: calcula o custo total das caixas
def custoTotalDeUmTipo(quantidade_caixas, preco_unitario):
    
    return quantidade_caixas * preco_unitario

def main():
    # Leitura dos dados de entrada
    total_garrafas = int(input("Total de garrafas: "))
    
    cap_basica = int(input("Capacidade da caixa básica: "))
    preco_basica = float(input("Preço da caixa básica: "))
    
    cap_reforcada = int(input("Capacidade da caixa reforçada: "))
    preco_reforcada = float(input("Preço da caixa reforçada: "))
    
    # Processamento com as funções
    qtd_basica = quantasDeUmTipo(total_garrafas, cap_basica)
    custo_basica = custoTotalDeUmTipo(qtd_basica, preco_basica)
    
    qtd_reforcada = quantasDeUmTipo(total_garrafas, cap_reforcada)
    custo_reforcada = custoTotalDeUmTipo(qtd_reforcada, preco_reforcada)
    
    # Exibição dos resultados
    print(f"\n--- Caixa Básica ---")
    print(f"Quantidade de caixas: {qtd_basica}")
    print(f"Custo total: R$ {custo_basica:.2f}")
    
    print(f"\n--- Caixa Reforçada ---")
    print(f"Quantidade de caixas: {qtd_reforcada}")
    print(f"Custo total: R$ {custo_reforcada:.2f}")


main()
