n = input('Digite seu nome:').upper()
#quantas letras a
print('No seu nome aparece {} letras A'.format(n.count('A')))
#posicao do primeiro a
print('O primeiro A aparece na posição {}'.format(n.find('A') + 1))
#posicao da ultima letra a
print('O ultimo A aparece na posição {}'.format(n.rfind('A') + 1))