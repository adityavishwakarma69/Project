import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import time

class MyBar(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="MyBar")
        self.set_default_size(400, 40)
        self.connect("destroy", Gtk.main_quit)

        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.add(self.box)

        self.label = Gtk.Label(label="")
        self.box.pack_start(self.label, True, True, 0)

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.set_text(current_time)
        return True

win = MyBar()
win.show_all()
Gtk.main()
