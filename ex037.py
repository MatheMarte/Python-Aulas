num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL\n')
escolha = int(input('Sua opção:' ))
if escolha == 1:
    print(bin(num)[2:])
elif escolha == 2:
    print(oct(num)[2:])
elif escolha == 3:
    print(hex(num)[2:])
else:
    print('Número inválido')
