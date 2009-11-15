import draw_gl as dg

from vec  import Vec

from OpenGL.GL   import * ## load OpenGL libraries


def draw_gl( self ):
    n = self.n
    r = self.r

    vt = Vec( 1,2,3 ).norm()
    if vt == n:
        vt = Vec( 3,2,1 ).norm()

    v1 = vt.vcross( n )
    v2 = v1.vcross( n )

    v1,v2,v3,v4 = r + v1+v2, r + v1-v2, r + v2-v1, r -v1-v2

    glBegin( GL_LINES )
    glVertex3f( *v1 )
    glVertex3f( *v4 )

    glVertex3f( *v2 )
    glVertex3f( *v3 )

    glVertex3f( *v1 )
    glVertex3f( *v2 )

    glVertex3f( *v1 )
    glVertex3f( *v3 )

    glVertex3f( *v3 )
    glVertex3f( *v4 )

    glVertex3f( *v2 )
    glVertex3f( *v4 )

    glEnd( )


import geom
geom.Plane.draw_gl = draw_gl
geom.Plane.opt = { 'color' : ( 0.8, 0.8, 0.8 ) }
