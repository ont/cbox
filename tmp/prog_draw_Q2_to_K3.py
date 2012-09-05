import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

import math
from vec   import *
from mat   import *
from zell  import *
from voron import *
from reper import *

import zell2reper

## drawing
import vec_gl
import voron_gl
from draw_gl import drawgl
from draw_ipe import drawipe


r = Zell( -1, -0, -1, -1, -2, -1 ).to_reper()
print r
vo = Voron( *r )
drawgl( vo )
drawgl.start()


drawipe.setup( 0, 0.2, 30 )

for x in xrange( 5 + 1 ):
    r = Zell( -1, -0, -1, -1, -2 + 0.4 * x, -1 ).to_reper()
    print r
    vo = Voron( *r )
    drawipe.group()   ## add each dirichlet cell to new group
    drawipe( vo )

drawipe.save( '/tmp/Q2_to_K3.ipe' )
