import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def Imprimir_algo(btn):
	print btn
	print 'Hola Mundo Cruel'

if __name__ == '__main__':

	ventana = Gtk.Window(title = 'Example_2')
	ventana.connect('delete-event', Gtk.main_quit)
	boton = Gtk.Button('Btn 1')
	#boton.connect('clicked', Imprimir_algo)
	boton_2 = Gtk.Button('Btn 2')
	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)
	contenedor.attach(
		boton,
		0,
		0,
		1,
		1,
		)
	contenedor.attach(boton_2, 0, 1, 1, 1)
	ventana.add(contenedor)
	ventana.add(boton)
	ventana.add(boton_2)
	ventana.show_all()

	Gtk.main()
