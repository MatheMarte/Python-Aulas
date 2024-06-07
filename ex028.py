import random

r = random.randint(1, 100)
n = int(input('Tente acertar o numero:'))
if n == r:
      print('Parabens voce acertou o numero!')
else:
     print('Poxa tente novamente... O número da vez era: {}'.format(r))
