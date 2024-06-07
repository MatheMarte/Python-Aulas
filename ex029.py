#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Em qual velocidade você está:'))
if v > 80:
    print('Você foi multado! A multa será no valor de R${}'.format(abs(80 - v)*7))
else:
    print('Tudo certo! Prossiga!')


