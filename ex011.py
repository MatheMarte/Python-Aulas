#programa largura e altura da parede
a = float(input('Qual a altura da parede:'))
l = float(input('qual a largura da parede:'))
#area
ar = a * l
print('Sua area e de {}m²'.format(ar))
#pintura
t = ar/2
print('Voce ira precisar de {} Litros de tinta para pintar'.format(t))