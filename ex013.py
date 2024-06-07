#de quem e o salario
nome = input('De quem e o salario:')
#salario
s = float(input('digite o salario atual de {}:'.format(nome)))
#aumento
au = (s * 0.15) + s
print('O novo salario de {} e: R${:.2f}'.format(nome, au))