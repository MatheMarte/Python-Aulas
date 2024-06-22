n = int(input('Digite um número para ver sua tabuada:'))
print('TABUADA DO {}'. format(n))
print('=-='*4)
for t in range(1,11):
    print('{} X {} = {}'.format(n, t, n * t))
print('=-='*4)
