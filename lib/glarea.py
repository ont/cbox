import gtk
import gtk.glade
import gtk.gtkgl

from OpenGL.GL import *
from OpenGL.GLU import *

class GLArea( gtk.DrawingArea, gtk.gtkgl.Widget ):
    def __init__( self ):
        gtk.DrawingArea.__init__( self )

        self.set_events(  gtk.gdk.EXPOSURE_MASK
                        | gtk.gdk.LEAVE_NOTIFY_MASK
                        | gtk.gdk.BUTTON_PRESS_MASK
                        | gtk.gdk.BUTTON_RELEASE_MASK
                        | gtk.gdk.POINTER_MOTION_MASK
                        | gtk.gdk.POINTER_MOTION_HINT_MASK )

        self.connect( "motion_notify_event",  self.on_motion_notify_event  )  ## mouse cursor moves
        self.connect( "button_press_event",   self.on_button_press_event   )  ## mouse button down...
        self.connect( "button_release_event", self.on_button_release_event )  ## mouse button up...
        self.connect( "expose_event",    self.on_expose_event    )            ## when widget is shown...
        self.connect( "configure_event", self.on_configure_event )            ## on changing sizes...



        display_mode = ( gtk.gdkgl.MODE_RGB | gtk.gdkgl.MODE_DOUBLE )  ## try to use double mode

        try:
            glconfig = gtk.gdkgl.Config( mode = display_mode )
        except gtk.gdkgl.NoMatches:
            display_mode &= ~gtk.gdkgl.MODE_SINGLE                     ## enabling single mode
            glconfig = gtk.gdkgl.Config( mode = display_mode )

        self.set_gl_capability( glconfig )                             ## ebabling config on gtkgl.Widget


        self.dist  = 3        ## distance to origin
        self.alpha = 0        ## angle to OX
        self.theta = 0        ## angle to OZ
        self.is_drag = False  ## when True mouse button is down


    def on_motion_notify_event( self, w, e ):
        if self.is_drag:
            ( dx, self.old_x ) = e.x - self.old_x, e.x
            ( dy, self.old_y ) = e.y - self.old_y, e.y
            self.alpha += dx * 1
            self.theta += dy * 1
            self.on_expose_event()


    def on_button_press_event( self, w, e ):
        self.old_x = e.x
        self.old_y = e.y
        self.is_drag = True


    def on_button_release_event( self, *args ):
        self.is_drag = False


    def polyline( self, verts, closed = False ):
        if closed:
            glBegin( GL_LINE_LOOP )
        else:
            glBegin( GL_LINE_STRIP )

        for v in verts:
            glVertex3f( v[0], v[1], v[2] )

        glEnd()


    def display( self ):
        glClearColor( 0,0,0,0 )
        glClear( GL_COLOR_BUFFER_BIT )
        glColor3f( 1,1,0 )
        self.polyline( [ ( -0.5, -0.5, 0 ), ( 0.5, -0.5, 0 ), ( 0.5, 0.5, 0 ), ( -0.5, 0.5, 0 ) ], closed = True )

        qobj = gluNewQuadric()
        gluSphere( qobj, 0.03, 40, 40 )


    def on_expose_event( self, *args ):

        gldrawable = self.get_gl_drawable()
        glcontext  = self.get_gl_context()
        if not gldrawable.gl_begin( glcontext ):
            return

        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

        glMatrixMode( GL_MODELVIEW )

        glLoadIdentity()
        glTranslatef( 0.0, 0.0, - self.dist )
        glRotatef( self.theta, 1.0, 0.0, 0.0 )
        glRotatef( self.alpha, 0.0, 1.0, 0.0 )

        self.display()

        gldrawable.swap_buffers()
        gldrawable.gl_end()


    def on_configure_event( self, widget, event ):
        print 'on_configure_event', event
        ( w, h ) = event.width, event.height

        gldrawable = self.get_gl_drawable()
        glcontext = self.get_gl_context()
        if not gldrawable.gl_begin( glcontext ):
            return

        glViewport( 0, 0, w , h )

        gluLookAt( 0.0,0.0,0.5, 0.0,0.0,0.0, 0.0, 1.0, 0.0 )
        glClearColor( 1.0, 1.0, 1.0, 1.0 )

        glMatrixMode( GL_PROJECTION )
        glLoadIdentity( )
        gluPerspective( 40, 1.0 * w / h, 0.1, 100.0 )


        gldrawable.gl_end()
