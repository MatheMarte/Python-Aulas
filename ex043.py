from time import sleep
print('-->'*6)
print('CALCULADORA DE IMC')
print('-->'*6)
sleep(1)
peso = float(input('Digite o seu peso(Kg):'))
altura = float(input('Digite sua altura(M):'))
imc = peso / (pow(altura,2))
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('PARABÉNS! Você está com o peso ideal!')
elif imc <= 30:
    print('Você está com sobrepeso!')
elif imc <= 40:
    print('Você está obeso!')
elif imc >= 45:
    print('Você está em obesidade mórbida!CUIDADO!')
