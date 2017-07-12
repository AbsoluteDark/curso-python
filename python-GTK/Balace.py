import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentanita(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentanita, self).__init__(*args, **kwargs)
		#self.set_default_size(500, 300)
		self.connect('delete-event', Gtk.main_quit)
		self.add_contenedor()
		self.add_entradaA()
		self.add_entradaP()
		self.add_botonA()
		self.add_botonP()
		self.add_listaA()
		self.add_listaP()

	def add_contenedor(self):	
		self.contenedor = Gtk.Grid()
		