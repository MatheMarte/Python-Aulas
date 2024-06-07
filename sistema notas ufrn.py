import heapq
mediaat = int(input('Digite a média atual:'))
vm = int(input('Digite a média mínima:'))
un = int(input('Quantas unidades você já fez:'))
if un == 1:
    u1 = float(input('Digite a nota da unidade 1:'))
    media = u1/3
    d2 = abs((u1 - (mediaat * 3)))/2
    print('Sua média é {:.1f}'.format(media))
    print('Para passar por média você precisa de {} nas'
          ' duas próximas unidades'.format(d2))
elif un == 2:
    u1 = float(input('Digite a nota da unidade 1:'))
    u2 = float(input('Digite a nota da unidade 2:'))
    media = (u1 + u2) / 3
    d2 = abs(((u1+u2) - (mediaat * 3)))
    print('Sua média é {:.1f}'.format(media))
    print('Para passar por média você precisa de {:.1f} na'
          'próxima unidade'.format(d2))
elif un == 3:
    u1 = float(input('Digite a nota da unidade 1:'))
    u2 = float(input('Digite a nota da unidade 2:'))
    u3 = float(input('Digite a nota da unidade 3:'))
    media = (u1 + u2 + u3) / 3
    d2 = abs(((u1+u2+u3) - (mediaat * 3)))
    if media < mediaat:
        if media < 6
            print('Sua média é {:.1f}'.format(media))
            print('Na quarta prova você precisará de {:.1f}'.format(vm))
        elif media < 5
            print('Sua média é {:.1f}'.format(media))
            print('Na quarta prova você precisará de {:.1f}'.format(vm - 1 ))
    elif d2 >= mediaat:
        print('Sua média é {:.1f}'.format(media))
        print('EBAAAAA! VOCÊ FOI APROVADO.')
    else:
        print('Sua média é {:.1f}'.format(media))
        print('Sinto muito. tu ta reprovado')