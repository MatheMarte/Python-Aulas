n = input('Digite seu nome completo:').strip().split()
print('Muito prazer, {}!'.format(n[0]))
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))