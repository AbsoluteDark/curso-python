import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentanita(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentanita, self).__init__(*args, **kwargs)
		self.set_default_size(500, 300)
		self.connect('delete-event', Gtk.main_quit)
		self.add_contenedor()
		self.add_entradaA()
		self.add_entradaP()
		self.add_botonA()
		self.add_botonP()
		self.add_listaA()
		self.add_listaP()
		#self.add_labelA()
		#self.add_labelP()
		#self.add_labelC()

	def add_contenedor(self):	
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def add_entradaA(self):	
		self.entradaA = Gtk.Entry()
		#self.entrada1.connect('activate', self.add_filaA)
		self.contenedor.attach(self.entradaA, 0, 0, 3, 1)
		self.entrada1 = Gtk.Entry()
		self.contenedor.attach(self.entrada1, 3, 0, 1, 1)

	#def add_labelA(self):	
		#self.labelA = 

	def add_entradaP(self):	
		self.entradaP = Gtk.Entry()
		self.contenedor.attach(self.entradaP, 0, 20, 3, 1)
		self.entrada2 = Gtk.Entry()
		self.contenedor.attach(self.entrada2, 3, 20, 1, 1)

	def add_botonA(self):	
		self.botonA = Gtk.Button('Activos')
		self.contenedor.attach_next_to(self.botonA, self.entradaA,
			Gtk.PositionType.BOTTOM,
			1,
			1)

		self.botonA.connect('clicked', self.add_filaA)


	def add_botonP(self):	
		self.botonP = Gtk.Button('Pasivos')
		self.contenedor.attach_next_to(self.botonP, self.entradaP,
			Gtk.PositionType.BOTTOM,
			1,
			2)

		self.botonP.connect('clicked', self.add_filaP)

	def add_listaA(self):	
		self.modeloA = Gtk.ListStore(str, float)
		self.lista_A = Gtk.TreeView(self.modeloA)

		descripcionA = Gtk.CellRendererText()
		columna_descripcionA = Gtk.TreeViewColumn('Descripcion_A', descripcionA, text=0)
		montoA = Gtk.CellRendererText()
		columna_montoA = Gtk.TreeViewColumn('Monto_A', montoA, text=1)

		self.lista_A.append_column(columna_descripcionA)
		self.lista_A.append_column(columna_montoA)

		self.contenedor.attach_next_to(self.lista_A, self.botonA,
			Gtk.PositionType.BOTTOM,
			1,
			1)

	def add_listaP(self):	
		self.modeloP = Gtk.ListStore(str, float)
		self.lista_P = Gtk.TreeView(self.modeloP)

		descripcionP = Gtk.CellRendererText()
		columna_descripcionP = Gtk.TreeViewColumn('Descripcion_P', descripcionP, text=0)
		montoP = Gtk.CellRendererText()
		columna_montoP = Gtk.TreeViewColumn('Monto_P', montoP, text=1)

		self.lista_P.append_column(columna_descripcionP)
		self.lista_P.append_column(columna_montoP)

		self.contenedor.attach_next_to(self.lista_P, self.botonP,
			Gtk.PositionType.BOTTOM,
			1,
			1)

	def add_filaA(self, btn):	
		textoA = self.entradaA.get_text()
		numeroA = self.entrada1.get_text()
		self.modeloA.append([textoA, float(numeroA)])

	def add_filaP(self, btn):		
		textoP = self.entradaP.get_text()
		numeroP = self.entrada2.get_text()
		self.modeloP.append([textoP, float(numeroP)])

if __name__ == '__main__':		
	ventana = MiVentanita()
	ventana.show_all()
	Gtk.main()
