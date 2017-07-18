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

if __name__ == '__main__':
	app = CursoPythonApp()
	app.run()
