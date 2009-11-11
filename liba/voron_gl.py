import draw_gl as dg

from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

import mesh_gl

def draw_gl( self ):
    # save old state and load identity matrix
    glPushMatrix()

    glTranslatef( *self.pos ) ## move coordinate system to center of polyhedra
    self.mesh.draw_gl()

    # load old transform matrix state
    glPopMatrix()


def draw( self, draw = True, **opt ):
    self.opt = {}
    self.opt.update( opt )
    dg.app.draw( self, draw )


import voron
voron.Voron.draw    = draw
voron.Voron.draw_gl = draw_gl
