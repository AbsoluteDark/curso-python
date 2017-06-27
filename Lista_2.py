numbers = [1,2,3,5,7,8,11,12,14,15,18,20,21,23,25,28,29,32,34,35]
lista_P = []
lista_I = []
while len(numbers) > 0:
	num = numbers.pop()
	lista_P.append(num)
else:
	lista_I.append(num)

	print('Numeros Pares: ')
	print(lista_P)
	lista_P.sort()
	print('Manera Ascendente: ', lista_P)

	print('Numeros Impares: ')
	print(lista_I)
	lista_I.sort()
	print('Manera Ascendente: ', lista_I)
	print(' <(*) ')
	