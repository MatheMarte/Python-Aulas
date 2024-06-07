n1= float(input('Primeira nota:'))
n2= float(input('Segunda nota:'))
media = (n1 + n2)/2
if media < 7:
    print('Tirando {} e {}, a média do aluno será {}.\n'
          'O aluno está em RECUPERAÇÃO'.format(n1, n2, media))
elif media >= 7:
    print('Tirando {} e {}, a média do aluno será {}.\n'
          'O aluno está APROVADO.'.format(n1, n2, media))
elif media < 5:
    print('Tirando {} e {}, a média do aluno será {}.\n'
          'O aluno está REPROVADO!'.format(n1, n2, media))