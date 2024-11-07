def calcular_emprestimo(valor, parcelas, taxa_juros):
    valor_total = valor * (1 + taxa_juros) ** parcelas

    valor_parcela = valor_total / parcelas
    return valor_total, valor_parcela

def exibir_detalhes_emprestimo(valor, parcelas, valor_total, valor_parcela, taxa_juros):
    print("\nDetalhes do Empréstimo:")
    print(f"Valor solicitado: R${valor:.2f}")
    print(f"Número de parcelas: {parcelas}")
    print(f"Taxa de juros: {taxa_juros * 100:.2f}% ao mês")
    print(f"Valor total a ser pago: R${valor_total:.2f}")
    print(f"Valor de cada parcela: R${valor_parcela:.2f}\n")

print("Bem-vindo ao sistema de empréstimos!")

try:
    valor = float(input("Digite o valor do empréstimo que deseja: R$"))
    parcelas = int(input("Digite o número de parcelas (entre 1 e 60): "))

    if parcelas < 1 or parcelas > 60:
        print("O número de parcelas deve estar entre 1 e 60.")
    else:
        tipo_emprestimo = input("Escolha o tipo de empréstimo (pessoal/consignado): ").strip().lower()

        if tipo_emprestimo == "pessoal":
            taxa_juros = 0.02  
        elif tipo_emprestimo == "consignado":
            taxa_juros = 0.01  
        else:
            print("Tipo de empréstimo inválido.")
            taxa_juros = None

        if taxa_juros is not None:
            valor_total, valor_parcela = calcular_emprestimo(valor, parcelas, taxa_juros)
            exibir_detalhes_emprestimo(valor, parcelas, valor_total, valor_parcela, taxa_juros)

except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")
