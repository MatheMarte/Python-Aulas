#Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
v = int(input('Digite a distância da sua viagem:').strip())
if v <= 200:
    print('Sua passagem custa R${}'.format(v*0.50))
else:
    print('Sua passagem custa R${}'.format(v*0.45))
