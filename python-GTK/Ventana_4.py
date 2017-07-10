import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500, 300)
		self.connect('delete-event', Gtk.main_quit)

	
	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()

		text = Gtk.Entry()
		text.get_text()
		boton = Gtk.Button('Resaltar el puto texto')
		label = Gtk.Label()
		label.set_markup()
		
if __name__ == '__main__':
	ventana = Gtk.Window(title = 'Pendejadas')
	ventana.add(contenedor)
	ventana.add(text)
	ventana.add(boton)
	ventana.add(label)
	ventana.show_all()

	Gtk.main()
