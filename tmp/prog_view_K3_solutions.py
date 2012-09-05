import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )


from mat   import *
from zell  import *
from voron import *
from reper import *

import zell2reper
import voron_gl

## drawing
from draw_gl import drawgl


#### definitions
pos = 0

def redraw():
    global pos, reps
    #### constructing sublattice reper
    #r1 = Zell( -1, 0, -1, -1, 0, -1 ).to_reper()
    r1, r2 = reps[ pos ]
    vo1 = Voron( *r1 )
    vo2 = Voron( *r2 )

    drawgl.clear()
    drawgl( vo1 )
    drawgl( vo2 )

    print r1, r2


def bnext( *args ):
    global pos, reps
    pos = pos < len( reps ) - 1 and pos + 1 or pos
    redraw()

def bprev( *args ):
    global pos, reps
    pos = pos > 1 and pos - 1 or pos
    redraw()

drawgl.button( 'next', bnext )
drawgl.button( 'prev', bprev )


#### loading matrices from file
reps = []
ls = open( 'solutions_K3-K3.txt' ).readlines()
ls.reverse()
while ls:
    ls.pop()

    mx = []
    for i in xrange( 3 ):
        t = ls.pop().split()
        mx.extend(  map( int, [ t[ 2 ], t[ 5 ], t[ 8 ] ] ) )
    mx = Mat( *mx )

    z = ls.pop().split()
    z = map( lambda x: float( x.rstrip( ',' ) )/100.0, [ z[ 3 ], z[ 5 ], z[ 7 ], z[ 9 ], z[ 11 ], z[ 13 ] ] )
    z = Zell( *z )

    reps.append( ( z.to_reper(), mx * z.to_reper() ) )


#### main loop
redraw()
drawgl.start()
