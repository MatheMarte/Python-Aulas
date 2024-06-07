import heapq
lista = (5,6,2)
print(sum(heapq.nlargest(2,lista)))

min = (u1, u2, u3)
nvm = abs((sum(heapq.nlargest(2, min)) / 3) - (mediaat * 3))