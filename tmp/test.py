import sys

import pygtk
pygtk.require('2.0')

import gtk
import gtk.glade

from glarea import GLArea

class MainGUI():
    def __init__( self, glade_file ):
        self.wtree = gtk.glade.XML( glade_file )
        self.wtree.signal_autoconnect( self )
        self.wnd_main = self.wtree.get_widget( 'wnd_main' )
        self.vbox_gl = self.wtree.get_widget( 'vbox_gl' )
        self.area_gl = GLArea()
        self.vbox_gl.pack_start( self.area_gl )
        self.wnd_main.show_all()
        #print dir( self.vbox_gl )


m_gui = MainGUI( 'tmp.glade' )
gtk.main()
