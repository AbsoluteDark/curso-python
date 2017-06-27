dato = (input("Ingresar el puto texto: "))
texto = dato
cuenta = 0
for char in texto:
	if char == 'e':
		print("El puto texto", dato, "tiene tantas", cuenta, "letras <e,E>")
		print("Capitalizacion: ", texto.upper())
		print(texto.replace('o', '0'), 'Reemplazamos la letra <o,O> por el numero <0>')
		print(" <(*) ")
		