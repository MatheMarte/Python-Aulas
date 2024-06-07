#leia o angulo
import math
ang = float(input('Digite seu angulo:'))
rad = math.radians(ang)
print('Seno:{:.2f}\nCosseno:{:.2f}\nTangente{:.2f}'
      .format(math.sin(rad), math.cos(rad), math.tan(rad)))
