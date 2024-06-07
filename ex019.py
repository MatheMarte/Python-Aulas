from random import choice
a = str(input('coloque o nome do aluno 1:'))
b = str(input('coloque o nome do aluno 2:'))
c = str(input('coloque o nome do aluno 3:'))
d = str(input('coloque o nome do aluno 4:'))
lista = [a, b, c, d]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))