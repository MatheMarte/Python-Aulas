#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. \Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for n in range (1,7):
    n = int(input('Digite seu {} número:'.format(n)))
    if n %2 == 0:
        soma = soma + n
        cont = cont + 1
        
print ('Você informou {} números PARES e a soma entre eles é {}'.format(cont, soma))
