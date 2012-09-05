import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from vec   import *
from mat   import *
from voron import *
from reper import *
from ucell import *

import reper2dots
import voron_inout
import voron_gl
import vec_gl

from draw_gl  import drawgl

## trans matrix
n = Mat( -3, -3, 0,
          0,  3, 0,
          2,  1, 3 )

r1 = Reper( Vec( -1,-1,0 ),
            Vec( 1,0,1 ),
            Vec( 0,1,1 ) )

r2 = n * r1

r2 = Reper( r2[0] + r2[2], r2[2] - r2[1], r2[2] )

vo1 = Voron( *r1 )
vo2 = Voron( *r2 )

ds1 = r1.to_dots( 5,5,5 )
ds2 = r2.to_dots( 2,2,2 )

drawgl( vo1 )
drawgl( vo2 )

for v in r2:
    drawgl( v, style ="line" )



for d in vo2.has( ds1 ):
    drawgl( d, r = 0.05, color=(0,1,0) )

for d in vo2.has( ds2 ):
    drawgl( d, r = 0.06, color=(1,0,0) )

drawgl.start()


print "%s %s %s" % tuple( r2[0] )
print "%s %s %s" % tuple( r2[1] )
print "%s %s %s" % tuple( r2[2] )

for d in vo2.has( ds2 ):
    print "b %s %s %s" % tuple( d )

for d in vo2.has( ds1 ):
    print "a %s %s %s" % tuple( d )

