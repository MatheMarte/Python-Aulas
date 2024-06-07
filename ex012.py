#preco do produto
p = float(input('Qual o preco do produto:'))
#desconto
d = p - (p * 0.05)
print('O valor com o desconto de 5% e: R${:.2f}'.format(d))
