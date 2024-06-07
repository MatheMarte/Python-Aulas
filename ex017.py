import math
#leia o comprimento do cateto oposto
a = float(input('Digite o valor do Cateto Oposto:'))
b = float(input('Agora, digite o valor do Cateto Adjascente:'))
#calcule a hipotenusa
h = math.sqrt(pow(a,2) + pow(b,2))
print('Aqui esta o valor da hipotenusa do seu triangulo retangulo:{:.2f}'.format(h))