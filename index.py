def calcular_pontos(vazamento):
    pesos = {'Senha': 100, 'Email': 15, 'Telefone': 70, 'Nome': 25}
    pontos = 0
    for dado, valor in vazamento.items():
        pontos += pesos.get(dado, 0) * valor
    return pontos

def rank_consum(vazamentos):
    rank = sorted(vazamentos.items(), key=lambda x: calcular_pontos(x[1]), reverse=True)
    return rank

def obter_dados():
    site = input("Digite o nome do site (Shopee, Mercado Livre, Shein): ")
    dados = {}
    while True:
        dado = input("Digite o tipo de dado vazado (Senha, Email, Telefone, Nome) ou 'exit' para encerrar: ").capitalize()
        if dado == 'Exit':
            break
        elif dado in ('Senha', 'Email', 'Telefone', 'Nome'):
            quantidade = int(input(f"Digite a quantidade de {dado}s vazados: "))
            dados[dado] = quantidade
        else:
            print("Tipo de dado inválido. Tente novamente.")
    return site, dados

def main():
    vazamentos = {}

    for _ in range(3):
        site, dados = obter_dados()
        vazamentos[site] = dados

    rank = criar_rank(vazamentos)

    print("\nRanking Decrescente:")
    for i, (site, pontos) in enumerate(rank, 1):
        print(f"{i}. {site}: {pontos} pontos")

if __name__ == "__main__":
    main()
