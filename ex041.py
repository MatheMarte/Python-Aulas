import datetime as dt
ano = int(input('Ano de nascimento:'))
atual = dt.date.today().year
dif = atual - ano
print('O atleta tem {} anos'.format(dif))
if dif <= 9:
    print('Classificação Mirim')
elif dif <=14: 
    print('Classificação Infantil')
elif dif <=19:
    print('Classificação Junior')
elif dif <=25:
    print('Classificação Sênior')
elif dif >=25:
    print('Classificação Master')
