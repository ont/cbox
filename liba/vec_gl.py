import draw_gl as dg

from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *


def draw_gl( self ):
    # save old state and load identity matrix
    glPushMatrix()

    if self.opt['style'] is 'dot':
        # move coordinate system to endpoint of vector
        glTranslatef( *self )

        # set sphere shiness
        glMaterialf( GL_FRONT, GL_SHININESS, 25.0 )

        # set reflection color
        specReflection = ( 0.7, 0.7, 0.7, 1.0 )
        glMaterialfv( GL_FRONT, GL_SPECULAR, specReflection )

        # set diffuse & ambient material colors
        glMaterialfv( GL_FRONT, GL_DIFFUSE, self.opt['color'] )
        glMaterialfv( GL_FRONT, GL_AMBIENT, ( 0.2, 0.2, 0.2 ) )

        qobj = gluNewQuadric()
        gluSphere( qobj, self.opt['r'], 40, 40 )

        # load old transform matrix state
        glPopMatrix()


def draw( self, draw = True, **opt ):
    self.opt = { 'style': 'dot', 'r': 0.03, 'color' : ( 0.8, 0.8, 0.8 ) }
    self.opt.update( opt )
    dg.app.draw( self, draw )


import vec
vec.Vec.draw    = draw
vec.Vec.draw_gl = draw_gl
