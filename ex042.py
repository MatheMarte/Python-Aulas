print('=-=' * 8)
print('ANALISADOR DE TRIÂNGULOS ATUALIZADO')
print('=-=' * 8)
p = float(input('Primeiro segmento:'))
s = float(input('Segundo segmento:'))
t = float(input('Terceiro segmento:'))
if t < p + s  and s < p + t  and p < s + t :
    if t == p == s:
        o = ('equilátero')
    elif t != p != s:
        o = ('escaleno')
    elif t == p or t == s or s == t :
        o = ('isósceles')
    print('Com os valores você consegue formar um triângulo {}'.format(o))
else:
    print('Com os valores você NÃO consegue formar um triângulo')
