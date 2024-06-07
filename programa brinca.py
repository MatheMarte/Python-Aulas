import random

r = random.randint(1, 100)
n1 = input('Player 1:')
n2 = input('Player 2:')
n3 = input('Player 3:')
num1 = int(input('{}, digite seu numero:'.format(n1)))
num2 = int(input('{}, digite seu numero:'.format(n2)))
num3 = int(input('{}, digite seu numero:'.format(n3)))
d1 = abs(r - num1)
d2 = abs(r - num2)
d3 = abs(r - num3)
m = min(d1,d2,d3)
print('O número escolhido foi {}'.format(r))
if m == d1:
    print('Parabéns, {}. Você é o ganhador'.format(n1))
elif m == d2:
    print('Parabéns, {}. Você é o ganhador'.format(n2))
else:
    print('Parabéns, {}. Você é o ganhador'.format(n3))