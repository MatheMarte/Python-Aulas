#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

preco = float(input('Valor das compras:'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
escolha = int(input('Digite sua opção:'))
if escolha == 1:
    print(' O desconto para R${:2f.} é 10%, o valor final é R${:.2f}'.format(preco, (preco-(0.1*preco))))
elif escolha == 2:
    print(' O desconto para R${:2f.} é 5%, o valor final é R${:.2f}'.format(preco, (preco-(0.05*preco))))