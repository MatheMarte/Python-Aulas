#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('digite um numero:'))
d = num * 2
t = num * 3
r = pow(num,(1/2))
print('O dobro de {}: {}. O triplo de {}: {}. A raiz quadrada de {}: {:.1f}.'.format(num, d, num, t, num, r))
