lista = []
for i in range(4):
	print("Digitar el numero", str(i+1) + ": ", end="")
	Digito = input()
	lista += [Digito]
	print("La lista creada es: ", lista)
	print("Primer numero de la lista es: ", lista[0])
	print("Ultimo numero de la lista es: ", lista[3])
	print(" <(*) ")
	