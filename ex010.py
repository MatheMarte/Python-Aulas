#leia dinheiro que a pessoa tem e mostre quantos dolares ela quer comprar.
din = float(input('Quanto dinheiro voce tem na carteira? R$'))
do = din / 3.27
print('Com R${} voce pode comprar US${:.2f}'.format(din, do))
