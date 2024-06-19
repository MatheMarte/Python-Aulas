from time import sleep
import random as rd
print("JOKENPÔ!")
sleep (0.5)
esc = int(input('Você quer jogar só ou com alguém? (1 ou 2):'))
if esc == 1:
    print("[0] PEDRA")
    print("[1] PAPEL")
    print("[2] TESOURA")
    p = int(input('SUA ESCOLHA:').strip())
    itens = ('Pedra', 'Papel', 'Tesoura' )
    pc = rd.randint(0,2)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('=_='*10)
    print('A sua jogada foi {}'.format(itens[p]))
    print('O computador escolheu {}'.format(itens[pc]))
    print('=_='*10)
    if pc == 0:
        if p == 0:
            print('EMPATE')
        elif p == 1:
            print('VOCÊ GANHOU!')
        elif p == 2:
            print('O COMPUTADOR GANHOU')
    if pc == 1:
        if p == 1:
            print('EMPATE')
        elif p == 2:
            print('VOCÊ GANHOU!')
        elif p == 0:
            print('O COMPUTADOR GANHOU')
    if pc == 2:
        if p == 2:
            print('EMPATE')
        elif p == 0:
            print('VOCÊ GANHOU!')
        elif p == 1:
            print('O COMPUTADOR GANHOU')
elif esc == 2:
    print("[0] PEDRA")
    print("[1] PAPEL")
    print("[2] TESOURA")
    p = int(input('JOGADOR 1 SUA ESCOLHA:').strip())
    p2 = int(input('JOGADOR 2 SUA ESCOLHA:').strip())
    itens = ('Pedra', 'Papel', 'Tesoura' )
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('=_='*10)
    print('O Jogador 1 escolheu {}'.format(itens[p]))
    print('O Jogador 2 escolheu {}'.format(itens[p2]))
    print('=_='*10)
    if p2 == 0:
        if p == 0:
            print('EMPATE')
        elif p == 1:
            print('O JOGADOR 1 GANHOU!')
        elif p == 2:
            print('O JOGADOR 2 GANHOU')
    elif p2 == 1:
        if p == 1:
            print('EMPATE')
        elif p == 2:
            print('O JOGADOR 1 GANHOU!')
        elif p == 0:
            print('O JOGADOR 2 GANHOU')
    elif p2 == 2:
        if p == 2:
            print('EMPATE')
        elif p == 0:
            print('O JOGADOR 1 GANHOU!')
        elif p == 1:
            print('O JOGADOR 2 GANHOU')
