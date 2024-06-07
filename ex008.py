#valor em metros e converta para centimetros e milimetros
m = float(input('digite seu valor em metros:'))
print('Seu valor em KM: {}.\nSeu valor em HM: {}.\nSeu valor em DECA: {}.'
      ' \nSeu valor em M: {}. \nSeu valor em DM:{}. \nSeu valor em CM:{}. \nSeu valor em MM:{}'
      .format(m/1000, m/100, m/10, m, m*10, m*100, m*1000))
