import random
lista = []
for i in range(20):
	lista.append(random.randint(0,100))

	print(lista)
	lista.sort()
	print('Orden Ascendente')
	print(lista)
	