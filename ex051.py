#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
soma = 0
primeirotermo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = primeirotermo + (10-1) * razao
for pa in range(primeirotermo, decimo+razao , razao):
    print(pa, end='-> ')
print('ACABOU')
