#programa que leia notas e de uma media de duas notas
n1 = float(input('digite sua primeira nota:'))
n2 = float(input('digite sua segunda nota:'))
m = (n1+n2)/2
print('Como sua primeira nota foi {:.1f}, e sua segunda nota foi {:.1f}... temos que sua media e {:.1f}'.format(n1, n2, m))