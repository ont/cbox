import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from vec   import *
from reper import *
from ucell import *
from math  import *

from draw_gl import drawgl

import ucell_min
import vec_gl

u = UCell( 1,1,1, pi/2, pi/2, pi/2 )
u.add( 'K', [ Vec( 0.0, 0.0, 0.0 ),
              Vec( 0.5, 0.5, 0.0 ),
              Vec( 0.5, 0.0, 0.5 ),
              Vec( 0.0, 0.5, 0.5 ),
              Vec( 0.5, 0.5, 1.0 ),
              Vec( 0.5, 1.0, 0.5 ),
              Vec( 1.0, 0.5, 0.5 ),
              Vec( 1.0, 0.0, 0.0 ),
              Vec( 0.0, 1.0, 0.0 ),
              Vec( 0.0, 0.0, 1.0 ),
              Vec( 1.0, 0.0, 1.0 ),
              Vec( 1.0, 1.0, 0.0 ),
              Vec( 0.0, 1.0, 1.0 ),
              Vec( 1.0, 1.0, 1.0 ),
              ] )

for v in u.pnts['K']:
    drawgl( v )

u.to_min()

drawgl.start()
