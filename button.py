import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ButtonWindow(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self, title="Button")
        self.set_border_width(10)

        hbox = gtk.Box(spacing=7)
        self.add(hbox)

        button = gtk.Button.new_with_label("Test")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = gtk.Button.new_with_mnemonic("_Open")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print("\"Test\" button was clicked")

    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")

    def on_close_clicked(self, button):
        print("Closing application")
        gtk.main_quit()

win = ButtonWindow()
win.connect("destroy", gtk.main_quit)
win.show_all()
gtk.main()
