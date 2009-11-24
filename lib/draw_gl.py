# -*- coding: utf8 -*-

import math

from vec import *

import gtk
import gtk.glade

import gtk.gtkgl
from OpenGL.GL  import *
from OpenGL.GLU import *


class GLArea( gtk.DrawingArea, gtk.gtkgl.Widget ):
    def __init__( self ):
        gtk.DrawingArea.__init__( self )

        self.set_events( gtk.gdk.BUTTON_MOTION_MASK | gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_RELEASE_MASK | gtk.gdk.BUTTON_PRESS_MASK )

        display_mode = ( gtk.gdkgl.MODE_RGB | gtk.gdkgl.MODE_DOUBLE | gtk.gdkgl.MODE_DEPTH )

        try:
            glconfig = gtk.gdkgl.Config( mode = display_mode )
        except gtk.gdkgl.NoMatches:
            display_mode &= ~gtk.gdkgl.MODE_SINGLE
            glconfig = gtk.gdkgl.Config( mode = display_mode )

        self.set_gl_capability( glconfig )

        self.connect( "expose_event"         , self.on_expose_event         )
        self.connect( "configure_event"      , self.on_configure_event      )
        self.connect( "scroll_event"         , self.on_scroll_event         )
        self.connect( "motion_notify_event"  , self.on_motion_notify_event  )
        self.connect( "button_press_event"   , self.on_button_press_event   )
        self.connect( "button_release_event" , self.on_button_release_event )

        self.objs    = []  ## this objs use API
        self.objs_gl = []  ## this objs draw by themselves

        self.drag  = False
        self.dist  = 10
        self.alpha = 21
        self.theta = 5
        self.sens  = ( 1.0, 1.0 )

        self.hook_select = None   ## hook function for on_select opengl object event



    def on_scroll_event( self, obj, evt ):
        delta = math.sqrt( self.dist ) / 5

        if evt.direction == gtk.gdk.SCROLL_UP and self.dist - delta > 0.5:
            self.dist -= delta
        elif self.dist + delta < 100:
            self.dist += delta

        self.queue_draw()



    def on_button_press_event( self, obj, evt ):
        #print dir( evt )
        if evt.button == 3:
            self.select( evt.x, evt.y )

        self.drag = True
        self.set_state( gtk.STATE_ACTIVE )
        self.lastx, self.lasty = evt.x, evt.y



    def on_button_release_event( self, *args ):
        self.drag = False
        self.set_state( gtk.STATE_NORMAL )



    def on_motion_notify_event( self, obj, evt ):
        if self.drag:
            x, y = evt.x, evt.y
            dx = self.lastx - x
            dy = self.lasty - y

            self.theta += -dy * self.sens[ 1 ]
            if abs( self.theta ) > 90:
                self.theta -= -dy * self.sens[ 1 ]
            self.alpha += -dx * self.sens[ 0 ]

            self.lastx, self.lasty = x, y
            self.queue_draw()



    def on_configure_event( self, obj, evt ):
        gldrawable = self.get_gl_drawable()
        glcontext  = self.get_gl_context()
        gldrawable.gl_begin( glcontext )

        self.width, self.height = evt.width, evt.height
        glViewport( 0, 0, evt.width, evt.height )

        glMatrixMode( GL_PROJECTION )
        glLoadIdentity()
        self.gl_projection()  ## setup projection matrix



    def on_expose_event( self, *args ):
        gldrawable = self.get_gl_drawable()
        glcontext  = self.get_gl_context()
        gldrawable.gl_begin( glcontext )

        glClearColor( 0,0,0,0 )
        glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()
        self.gl_modelview() ## setup model matrix

        self.gl_colors()    ## setup opengl colors
        self.display()      ## draw scene

        gldrawable.swap_buffers()
        gldrawable.gl_end()



    def gl_colors( self ):
        glEnable( GL_DEPTH_TEST )

        glEnable( GL_LIGHTING )
        glEnable( GL_LIGHT0 )
        glEnable( GL_LIGHT1 )
        # parametrs for LIGHT0
        # +---------->      R       G      B    Alpha
        ambientLight  =  ( 0.0  ,  0.0 ,  0.0 , 1.0 )
        diffuseLight  =  ( 0.7  ,  0.7 ,  0.7 , 1.0 )
        specularLight =  ( 0.8  ,  0.8 ,  0.8 , 1.0 )
        position      =  ( 1.5  , -1.0 ,  4.0 , 1.0 )
        # assign created components to GL_LIGHT0
        glLightfv( GL_LIGHT0, GL_AMBIENT,  ambientLight )
        glLightfv( GL_LIGHT0, GL_DIFFUSE,  diffuseLight )
        glLightfv( GL_LIGHT0, GL_SPECULAR, specularLight )
        glLightfv( GL_LIGHT0, GL_POSITION, position )
        # parametrs for LIGHT1
        # +---------->      R       G      B    Alpha
        ambientLight  =  ( 0.0  ,  0.0 ,  0.0 , 1.0 )
        diffuseLight  =  ( 0.7  ,  0.7 ,  0.7 , 1.0 )
        specularLight =  ( 0.8  ,  0.8 ,  0.8 , 1.0 )
        position      =  (-1.5  , -1.0 ,  -4.0 , 1.0 )
        # assign created components to GL_LIGHT0
        glLightfv( GL_LIGHT1, GL_AMBIENT,  ambientLight )
        glLightfv( GL_LIGHT1, GL_DIFFUSE,  diffuseLight )
        glLightfv( GL_LIGHT1, GL_SPECULAR, specularLight )
        glLightfv( GL_LIGHT1, GL_POSITION, position )



    def gl_modelview( self ):
        glTranslatef( 0.0, 0.0, -self.dist )
        glRotatef( self.theta, 1.0, 0.0, 0.0 )
        glRotatef( self.alpha, 0.0, 1.0, 0.0 )



    def gl_projection( self ):
        gluPerspective( 40, 1.0 * self.width / self.height, 0.1, 100.0 )



    def select( self, x, y ):
        glSelectBuffer( len( self.objs )*10 ) ## allocate a selection buffer
        glRenderMode( GL_SELECT )             ## change to select mode
        glInitNames()

        glMatrixMode( GL_PROJECTION )
        glPushMatrix()   ## save projection matrix
        glLoadIdentity()

        gluPickMatrix( x, self.height - y, 2.0, 2.0, glGetIntegerv( GL_VIEWPORT ) )  ## first init pick transform
        self.gl_projection()                                                         ## ... and only now do projection !!!

        ## setup camera rotation and translation
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()
        self.gl_modelview()

        ## draw in select mode
        objs = self.objs + self.objs_gl
        for i,o in enumerate( objs ):
            glPushName( i )  ## new object start to draw
            if hasattr( o, 'draw' ):
                glPushMatrix()
                o.draw( self.api )
                glPopMatrix()
            else:
                o.draw_gl( )
            glPopName( i )   ## end of object

        glMatrixMode( GL_PROJECTION )
        glPopMatrix()   ## restore projection matrix


        buff = glRenderMode( GL_RENDER )          ## take info about selected objects
        if buff:
            nobj = min( buff, key = lambda b: b[1] )  ## take nearest object
            nobj = nobj[2][0]                         ## take object id
            if nobj and self.hook_select:
                self.hook_select( objs[ nobj ] )      ## pass to hook selected object


    def display( self ):
        ## draw by ip
        for o in self.objs:
            glPushMatrix()
            o.draw( self.api )
            glPopMatrix()

        ## draw by themselves
        map( lambda o: o.draw_gl( ), self.objs_gl )



class DrawGL( object ):
    def __init__( self, gfile ):
        self.wtree = gtk.glade.XML( gfile )    ## load widget tree from glade
        self.wtree.signal_autoconnect( self )  ## connect all event-handlers

        wt = self.wtree                                 ## more short
        self.wnd_main  = wt.get_widget( 'wnd_main'  )   ## .. paths to widgets
        self.vbox_btns = wt.get_widget( 'vbox_btns' )   ## box for user-defined buttons
        self.vbox_gl   = wt.get_widget( 'vbox_gl'   )

        self.gl     = GLArea() ## create opengl area
        self.gl.api = self     ## store api for it
        self.vbox_gl.pack_start( self.gl )

        self.wnd_main.show_all()


    def __call__( self, obj, **opt ):
        if not hasattr( obj, 'draw' ) and not hasattr( obj, 'draw_gl' ):
            raise Exception, "Object %s can't be drawn" % obj

        optt = dict( getattr( obj, 'opt', {} ) )  ## take a copy of default values
        optt.update( opt )                        ## change default values
        obj.opt = optt                            ## save it to object

        if hasattr( obj, 'draw' ):         ## this obj use standart API
            self.gl.objs.append( obj )

        if hasattr( obj, 'draw_gl' ):      ## obj use special opengl featrues
            self.gl.objs_gl.append( obj )

        self.gl.queue_draw()


    def clear( self ):
        self.gl.objs    = []
        self.gl.objs_gl = []
        self.gl.queue_draw()


    ################# OpenGL API #################
    def proj( self, v ):
        return Vec( *gluProject( *v ) )


    def trans( self, v ):
        """ Move coordinate system to point v.
        """
        glTranslatef( *v )


    def line( self, v1, v2, color, **opt ):
        glDisable( GL_LIGHTING )      ## disable lightings for lines
        glEnable( GL_COLOR_MATERIAL )

        glColor3f( *color );
        glBegin( GL_LINES )
        glVertex3f( *v1 )
        glVertex3f( *v2 )
        glEnd( )

        glDisable( GL_COLOR_MATERIAL )
        glEnable( GL_LIGHTING )       ## enabling lighting


    def sphere( self, pos, r, color, **opt ):
        # move coordinate system to endpoint of vector
        glTranslatef( *pos )

        # set sphere shiness
        glMaterialf( GL_FRONT, GL_SHININESS, 25.0 )

        # set reflection color
        specReflection = ( 0.7, 0.7, 0.7, 1.0 )
        glMaterialfv( GL_FRONT, GL_SPECULAR, specReflection )

        # set diffuse & ambient material colors
        glMaterialfv( GL_FRONT, GL_DIFFUSE, color )
        glMaterialfv( GL_FRONT, GL_AMBIENT, ( 0.2, 0.2, 0.2 ) )

        qobj = gluNewQuadric()
        gluSphere( qobj, r, 30, 30 )



    def start( self ):
        gtk.main()


    def button( self, text, func ):
        """ Create user defined button
            func: callback function
        """
        btn = gtk.Button( text )
        btn.connect( "clicked", func )
        btn.set_size_request(80, 35)

        self.vbox_btns.pack_start( btn,
                                   False,   ## .. no expand
                                   False )  ## .. no fill
        self.vbox_btns.show_all()


    def select( self, func ):
        self.gl.hook_select = func


    def on_close( self, *args ):
        gtk.main_quit()





import os.path as p

drawgl = DrawGL( p.dirname( p.abspath( __file__ ) ) + '/draw_gl.glade' )
#app.wnd_main.present()
#app.wnd_main.set_keep_above( True )

