import locale
from locale import gettext as _

import pygame
import tileset
from gi.repository import Gtk
from gi.repository import GLib
import os
import sys

def enum(**enums):
	return type('Enum', (), enums)
	
View = enum(Auto=None, CLASSIC='classic_view', MODERN='modern_view')
session = os.getenv("DESKTOP_SESSION")

class MyWindow(Gtk.ApplicationWindow):
	ui_file = 'Map_editor.glade'
	
	def __init__(self):
		Gtk.Window.__init__(self, title=_("MapEditor"), application=app)
		builder = Gtk.Builder()
		builder.add_from_file(self.ui_file)
		win = builder.get_object('window1')
		win.get_children()[0].reparent(self)
		#win.show_all()

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        self.win = MyWindow()
        self.win.show_all()

    def do_startup (self):
        # start the application
        Gtk.Application.do_startup(self)
        
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
