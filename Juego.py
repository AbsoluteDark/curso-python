import random
from time import sleep
print "Bienvenido, vamos a jugar a Piedra, papel o tijera."
print ""
sleep(3)
print "Jugamos al mejor de tres, o te gustaria cambiar?"
sleep(5)
print ""

def juego(intentos):
 x = 0
 tu = 0
 pc = 0
 while str(x) != intentos:
  print "Piedra, papel o tijera?"
  opcion = raw_input()
  opcion = opcion.lower()
  azar = random.choice(["piedra", "papel", "tijera"])
  if opcion == azar:
   print "La PC tambien escogio", azar
   print ""
  elif azar == "tijera" and opcion == "papel":
   x += 1
   pc += 1
   print ("LA PC saco", azar)
   print "Usted", tu, "La PC", pc
   print ""
  elif azar == "tijera" and opcion == "piedra":
   x += 1
   tu += 1
   print "La PC saco", azar
   print "Usted", tu, "La PC", pc
   print ""
  elif azar == "piedra" and opcion == "tijera":
   x += 1
   pc += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "piedra" and opcion == "papel":
   x += 1
   tu += 1
   print "La PC saco", azar
   print "Usted", tu, "La PC", pc
   print ""
  elif azar == "papel" and opcion == "tijera":
   x += 1
   tu += 1
   print "La PC saco", azar
   print "Usted", tu, "La PC", pc
   print ""
  elif azar == "papel" and opcion == "piedra":
   x += 1
   pc += 1
   print "La pc saco", azar
   print "Usted", tu, "La PC", pc
   print ""
  else:
   print "Dato mal introducido__Intentelo de nuevo"
 
 print ""
 
 if pc > tu:
  print "Gano la PC", pc, "con ventaja de =>", tu
 elif pc == tu:
  print "Empataron", tu, "a", pc
 else:
  print "Gano usted", tu, "con ventaja de =>", pc
 
 print ""
 print "PARTIDA TERMINADA"
 
 
def main():
 print "Escribe 1 para jugar al mejor de tres."
 print "Escribe 2 para cambiar el tipo de juego."

 opcion = raw_input()

 if opcion == 1:
  juego("3")
  print ("")
  restart = raw_input("Quieres jugar de nuevo?(s/n): ")
  restart = restart.lower()
  if restart == "s":
   print ""
   main()
 else:
  intentos = raw_input("Jugamos al mejor de: ")
  juego(intentos)
  print ("")
  restart = raw_input("Quieres jugar de nuevo?(s/n): ")
  restart = restart.lower()
  if restart == "s":
   print ""
   main()
  else:
   print "FIN"
 
main()