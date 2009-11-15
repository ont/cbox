import draw_gl as dg

from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

import mesh_gl


#def draw_gl( self ):
#    # save old state and load identity matrix
#    glPushMatrix()
#
#    glTranslatef( *self.pos ) ## move coordinate system to center of polyhedra
#    self.mesh.draw_gl()
#
#    # load old transform matrix state
#    glPopMatrix()


def draw( self, api ):
    api.trans( self.pos )
    self.mesh.draw( api )


import voron
voron.Voron.draw = draw
