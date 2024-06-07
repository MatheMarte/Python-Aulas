print('=-=' * 8)
print('ANALISADOR DE TRIÂNGULOS')
print('=-=' * 8)
p = float(input('Primeiro segmento:'))
s = float(input('Segundo segmento:'))
t = float(input('Terceiro segmento:'))
if t < p + s  and s < p + t  and p < s + t :
    print('Com os valores você consegue formar um triângulo')
else:
    print('Com os valores você NÃO consegue formar um triângulo')