#ler nome completo
nome = input('Coloque seu nome completo:')
#nome com todas maiusculas
maius = nome.upper()
#nome com todas minusculas
minus = nome.lower()
#quantas letras sem considerar espacos
split = nome.split()
join = ''.join(split)
#qunantas letras tem o primeiro nome
prim = nome.split()
#mostrar
print("""Aqui está seu nome com os fatores alterados:\nCom letras maiúsculas:{}\n
Com letras minúsculas:{}\nQuantas letras:{}\nLetras no primeiro nome:{}"""
      .format(maius, minus, len(join), len(prim[0])))