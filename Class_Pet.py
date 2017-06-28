class Mascotas(object):
	def __init__(self, nombre):
		self.nombre = nombre 

		def get_name(self):
			print 'Dentro de la primera Clase'
			return '{nombre}'.format(nombre=self.nombre)

class Perro(Mascotas):
    def __init__(self, nombreP):
        self.nombreP = nombreP

    def get_name(self):
        return self.nombreP    			

class Gato(Mascotas):
    def __init__(self, nombreG):
        self.nombreG = nombreG

    def get_name(self):
        return self.nombreG

class Domesticos(Perro, Gato):
	A = 'un Attrib'

	def __init__(self, tipo, semejanza):
		super(Domesticos, self).__init__(semejanza)
		self.tipo = tipo

	def obtener_tipo(self):
	    return self.tipo

	def obtener_semejanza(self):
	    print 'Metodo de mismo comportamiento'
	    semejanza = super(Domesticos, self).obtener_semejanza()
	    print semejanza
	    return semejanza    	

if __name__ == '__main__':
    nombreP = Perro('MarmaDuke')
    nombreG = Gato('Garfield') 
    print nombreP.get_name()
    print nombreG.get_name()

    pet = Domesticos('Mascotas', 'Se Odian')
    print pet.get_name()
