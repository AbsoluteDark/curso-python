import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500, 300)
		self.connect('delete-event', Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_entrada()
		self.agregar_boton()
		self.agregar_lista()
		#self.agregar_fila()

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):	
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0, 0, 1, 1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			1,
			1
			)

		self.boton.connect('clicked', self.agregar_fila)

	def agregar_lista(self):	

		self.modelo = Gtk.ListStore(str, float)
		self.modelo.append(['Valor_1', 1.5])
		self.lista_archivos = Gtk.TreeView(self.modelo)

		descripcion = Gtk.CellRendererText()
		columna_descripcion = Gtk.TreeViewColumn('Descripcion', descripcion, text=0)

		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

		self.lista_archivos.append_column(columna_descripcion)
		self.lista_archivos.append_column(columna_monto)

		self.contenedor.attach_next_to(
			self.lista_archivos,
			self.boton,
			Gtk.PositionType.BOTTOM,
			1,
			1)

		self.modelo.append(['Valor_1', 1.5])

	def agregar_fila(self, btn):	
		text = self.entrada.get_text()
		self.modelo.append([text, 1.5])

if __name__ == '__main__':	
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
	