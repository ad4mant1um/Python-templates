import gi
gi.require_version('gtk', '3.0')
from gi.repository import gtk

win = gtk.MyWindow()
win.connect("destroy", gtk.main_quit)
win.show_all()
gtk.main()
