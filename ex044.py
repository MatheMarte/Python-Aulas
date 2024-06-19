preco = float(input("Valor das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/cheque")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

escolha = int(input("Digite sua opção: "))

if escolha == 1:
    desconto = preco * 0.1
    valor_final = preco - desconto
    print(f"O desconto para R${preco:.2f} é de 10%, o valor final é R${valor_final:.2f}")
elif escolha == 2:
    desconto = preco * 0.05
    valor_final = preco - desconto
    print(f"O desconto para R${preco:.2f} é de 5%, o valor final é R${valor_final:.2f}")
elif escolha == 3:
    valor_parcela = preco / 2
    print(f"Para o valor do parcelamento escolhido não tem desconto disponível. O valor de cada parcela é R${valor_parcela:.2f}. Sendo o valor final R${preco:.2f}")
elif escolha == 4:
    numero_parcelas = int(input("Digite quantas parcelas: "))

    if numero_parcelas < 3:
        print("Número de parcelas indisponível. Escolha acima de 3x.")
    else:
        taxa_juros = 0.2  # Taxa de juros mensal (em decimal, ex: 0.05 para 5%)
        valor_parcela = (preco * taxa_juros + preco ) / numero_parcelas
        valor_final = preco + (taxa_juros * preco)

        print(f"""
            Sua compra vai ser parcelada em {numero_parcelas}x de R${valor_parcela:.2f} COM JUROS:
            * Valor final: R${valor_final:.2f}
            """)
else:
    print("Opção inválida. Tente novamente.")

