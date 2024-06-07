import datetime
atual = datetime.date.today().year
ano = int(input('Ano de nascimento:'))
idade = abs(ano-atual)
if idade < 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    print('Ainda faltam {} anos para o alistamento.'.format(abs(idade - 18)))
    print('Seu alistamento será em {}.'.format(ano + 18))
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    print('Você já deveria ter se alistado há {} ano(s)'.format(abs(idade - 18)))
    print('Seu alistamento foi em {}'.format(ano + 18))
else:
    print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    print('Seu alistamento é esse ano! Vá se alistar.')