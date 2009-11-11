import gtk
import gtk.glade
import gtk.gtkgl

from OpenGL.GL import *
from OpenGL.GLU import *

class GLArea( gtk.DrawingArea, gtk.gtkgl.Widget ):
    def __init__( self ):
        gtk.DrawingArea.__init__( self )

        ## whats to listen...
        self.set_events( gtk.gdk.BUTTON_MOTION_MASK  |  gtk.gdk.KEY_PRESS_MASK      | gtk.gdk.KEY_RELEASE_MASK |
                         gtk.gdk.POINTER_MOTION_MASK |  gtk.gdk.BUTTON_RELEASE_MASK |
                         gtk.gdk.BUTTON_PRESS_MASK   |  gtk.gdk.SCROLL_MASK )

        display_mode = ( gtk.gdkgl.MODE_RGB | gtk.gdkgl.MODE_DOUBLE )  ## try to use double mode

        try:
            glconfig = gtk.gdkgl.Config( mode = display_mode )
        except gtk.gdkgl.NoMatches:
            display_mode &= ~gtk.gdkgl.MODE_SINGLE                     ## enabling single mode
            glconfig = gtk.gdkgl.Config( mode = display_mode )

        self.set_gl_capability( glconfig )                             ## ebabling config on gtkgl.Widget

        self.connect( "expose_event",    self.on_expose_event    )     ## when widget is shown...
        self.connect( "realize",         self.on_realize         )     ## on creating resources...
        self.connect( "configure_event", self.on_configure_event )     ## on changing sizes...


    def polyline( self, vertexes_list, closed = False ):
        if closed:
            glBegin( GL_LINE_LOOP )
        else:
            glBegin( GL_LINE_STRIP )

        for vertex in vertexes_list:
            glVertex3f( vertex[0], vertex[1], 0 )

        glEnd()

    def display( self ):
        glClearColor( 0,0,0,0 )
        glClear( GL_COLOR_BUFFER_BIT )
        glColor3f( 1,1,0 )
        self.polyline( [ ( -10, -10 ), ( 10, -10 ), ( 10, 10 ), ( -10, 10 ) ], closed = True )


    def on_expose_event( self, *args ):
        print 'on_expose_event'
        gldrawable = self.get_gl_drawable()
        glcontext  = self.get_gl_context()
        if not gldrawable.gl_begin( glcontext ):
            return
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()

        self.display()

        gldrawable.swap_buffers()
        gldrawable.gl_end()


    def on_realize( self, *args ):
        print 'on_realize'


    def on_configure_event( self, widget, event ):
        print 'on_configure_event', event
        ( w, h ) = event.width, event.height

        gldrawable = self.get_gl_drawable()
        glcontext = self.get_gl_context()
        if not gldrawable.gl_begin( glcontext ):
            return

        glViewport( 0, 0, max( w, h ) , max( w, h ) )
        gluLookAt( 0.0,0.0,0.5, 0.0,0.0,0.0, 0.0, 1.0, 0.0 )

        glClearColor( 1.0, 1.0, 1.0, 1.0 )
        glMatrixMode( GL_PROJECTION )
        glLoadIdentity()


        glOrtho( -40, 40, -40, 40, -1, 1 )

        gldrawable.gl_end()                       #fine dei comandi Grafica
