import draw_gl as dg

from vec  import Vec
from mesh import Poly
# load OpenGL libraries
from OpenGL.GL   import *
from OpenGL.GLU  import *


def draw_gl( self ):
    def gl_line( s, e, color = None ):
        if color == None:
            glColor3f( 1.0, 1.0, 1.0 );
        else:
            glColor3f( color[ 0 ], color[ 1 ], color[ 2 ] );

        glBegin( GL_LINES )
        glVertex3f( *s )
        glVertex3f( *e )
        glEnd( )


    # save old OpenGL state...
    glPushMatrix()

    glDisable( GL_LIGHTING )     ## disable lightings for lines
    glEnable( GL_COLOR_MATERIAL )

    #glScalef( self.scale, self.scale, self.scale )

    np_pm = glGetDoublev( GL_PROJECTION_MATRIX )
    np_mv = glGetDoublev( GL_MODELVIEW_MATRIX  )

    visible = set()

    apnts = [ d for p in self.polys for d in p.pnts ]
    cv = reduce( lambda a,b: a+b, apnts )
    cv = 1 / len( apnts ) * cv
    cv = gluProject( *cv )
    cv = Vec( *cv )

    for i,p in enumerate( self.polys ):
        pnts = p.pnts[ 0:3 ]
        pnts = map( lambda p: Vec( *gluProject( p.x, p.y, p.z ) ), pnts )
        p_temp = Poly( pnts )
        n_temp = p_temp.norm( bvec = cv )

        if n_temp[ 2 ] < 0:
            visible.update( p.edgs )

    color = getattr( self, 'color', None )

    for e in self.uedgs:
        c = color if e in visible else ( 0.3, 0.3, 0.3 )
        gl_line( e.p1, e.p2, c )

    glDisable( GL_COLOR_MATERIAL )  ## enabling lighting
    glEnable( GL_LIGHTING )

    # load old transform matrix state
    glPopMatrix()


def draw( self, draw = True ):
    dg.app.draw( self, draw )


import mesh
mesh.Mesh.draw    = draw
mesh.Mesh.draw_gl = draw_gl
