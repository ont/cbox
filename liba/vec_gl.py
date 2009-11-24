import draw_gl as dg

from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *


def draw( self, api ):
    # save old state and load identity matrix
    if self.opt['style'] is 'dot':
        api.sphere( self, self.opt['r'], self.opt['color'] )

    if self.opt['style'] is 'line':
        api.line( self.opt['start'], self, self.opt['color'] )




import vec
vec.Vec.draw = draw
vec.Vec.opt = { 'style' : 'dot',
                'r'     : 0.03,
                'color' : ( 0.8, 0.8, 0.8 ),
                'start' : vec.Vec( 0,0,0 ) }
