#rie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número inteiro:').strip())
s = n % 2
if s == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é IMPAR!'.format(n))