class Persona(object):
	def __init__(self, nombre, apellido='asdfasdf'):
		self.nombre = nombre
		self.apellido = apellido

	def obtener_nombre(self):
		print 'Dentro de clase base'
		return '{nombre} {apellido}'.format(
            nombre=self.nombre,
            apellido=self.apellido
        )
#def otro_metodo(cls): #	print 'hola'
class PersonaNicaragua(object):
	def __init__(self, id):
		self.id = id

	def obtener_id(self):
		return self.id

class Estudiante(Persona, PersonaNicaragua):
    a = 'un attrb'
    def __init__(self, curso, nombre):
    	super(Estudiante, self).__init__(nombre)
        self.curso = curso

    def obtener_curso(self):

    	return self.curso

    def obtener_nombre(self):
    	print 'metodo de subclase'
        nombre = super(Estudiante, self).obtener_nombre()
        print nombre
        return nombre
 
if __name__ == '__main__':

    estudiante  = Estudiante('programacion', 'Otro nombre')
    print estudiante.obtener_nombre()
