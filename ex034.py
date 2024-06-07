nome = input('Digite seu nome:')
s = float(input('Olá, {}! Digite o valor do seu salário:'.format(nome)))
if s > 1250:
    print('O valor do seu salário com o aumento fica R${:.2f} '.format((s * 0.1) + s ))
else:
    print('O valor do seu salário com o aumento fica R${:.2f} '.format((s * 0.15) + s))