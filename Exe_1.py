import argparse

if __name__ == '__main__':
   parse = argparse.ArgumentParser('val')
   parser.add_argument('Nombre')
   parser.add_argument('Edad')
   parser.add_argument('Curso')
   
   args = parser.parse_args()
   
   datos = {
     'Nombre': args.Nombre,
     'Edad': args.Edad,
     'Curso': args.Curso
   }
   
   for llave, valor in datos.iteritems():
     print llave, valor