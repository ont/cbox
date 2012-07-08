import draw_gl as dg

import vec
from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *


def draw( self, api ):
    cols = [ (1,0,0), (0,1,0), (0,0,1) ]
    for v,c in zip( self, cols ):
        api.line( vec.Vec( 0,0,0 ), v, c )




import reper
reper.Reper.draw = draw
#reper.Reper.opt = { 'style' : 'dot',
#                    'r'     : 0.3,
#                    'color' : ( 0.8, 0.8, 0.8 ),
#                    'start' : vec.Vec( 0,0,0 ) }
