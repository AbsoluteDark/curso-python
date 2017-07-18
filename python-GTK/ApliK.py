import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GLib
from Balace import MiVentanita

class CursoPythonApp(Gtk.Application):
	def __init__(self, *args, **kwargs):
		super(CursoPythonApp, self).__init__(
			*args,
			application_id = 'ni.edu.udem.curso-python.ATM',
			**kwargs)
		self.window = None

	def do_activate(self):	
		if not self.window:
			self.window = MiVentanita(application=self, title='Main_Window')
			self.window.show_all()
			self.window.present()

	def do_startup(self):		
		Gtk.Application.do_startup(self)
		accion_otra_ventana = Gio.SimpleAction.new('Balance_General', None)
		accion_otra_ventana.connect('activate', self.crear_balance)
		self.add_action(accion_otra_ventana)

		builder = Gtk.Builder.new_from_file('menu.xml')
		self.set_app_menu(builder.get_object('App_Menu'))

	def crear_balance(self, action, params):	
		print 'Una_Puta_Accion'


if __name__ == '__main__':
	app = CursoPythonApp()
	app.run()
