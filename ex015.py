#quantidade de dias alugados
d = int(input('Quantos dias alugados?'))
#pergunte a quantidade de km
k = float(input('Quantos KMs rodados?'))
pago = (d * 60) + (k * 0.15)
print('Total a pagar: R${:.2f} '.format(pago))