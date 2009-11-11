import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

import draw_gl

from vec   import *
from zell  import *
from voron import *
from spgrp import *
from reper import *

import vec_gl
import voron_gl
import spgrp_wyck
import zell2reper
import voron_inout
import reper_coord

#vo = Voron( Vec( 0.0, 0.5, 0.5 ),
#            Vec( 0.5, 0.0, 0.5 ),
#            Vec( 0.5, 0.5, 0.0 ) )
#
#vo.draw()
#
#s  = SpGrp( 225, 1 )
#
#cols = [ ( 1, 0, 0 ),
#         ( 0, 1, 0 ),
#         ( 0, 0, 1 ),
#         ( 1, 1, 0 ),
#         ( 1, 0, 1 ),
#         ( 0, 1, 1 ),
#         ( 1, 1, 1 ),
#         ( 0.5, 0.5, 0.5 )]
#for iw, w in enumerate( s.wyckiter() ):
#
#    for iv, v in enumerate( vo.cut( w ) ):
#        v.draw( color = cols[ iw ] )
#        print 'draw vector...', v




r1 = Reper( Vec( 0.3, 0.0, 0.0 ),
            Vec( -0.1, 0.282842712475, 0.0 ),
            Vec( -0.1, -0.141421356237, 0.244948974278 ) )
r2 = Reper( Vec( -0.5, 0.565685424949, -0.489897948557 ),
            Vec( 0.7, -0.282842712475, -0.489897948557 ),
            Vec( -0.5, -0.707106781187, 0.244948974278 ) )
v1 = (r2.v1 + r2.v2)
v2 = (r2.v1 + r2.v3)
v3 = v1.norm().vcross( v2.norm() ) * v1.vlen()
r3 = Reper( v1,v2,v3 )

v1 = (r1.v1 + r1.v2)
v2 = (r1.v1 + r1.v3)
v3 = v1.norm().vcross( v2.norm() ) * v1.vlen()
r4 = Reper( v1,v2,v3 )


r1 = r1.minimize()
r2 = r2.minimize()

vo1 = Voron( r1.v1, r1.v2, r1.v3 )
vo2 = Voron( r2.v1, r2.v2, r2.v3 )
vo3 = Voron( r3.v1, r3.v2, r3.v3 )
vo4 = Voron( r4.v1, r4.v2, r4.v3 )


vo1.draw()
#vo2.draw()
vo3.draw()
vo4.draw()

#pnts = set()
#for a,b,c in ( (i,j,k) for i in xrange( -3,4 )\
#                       for j in xrange( -3,4 )\
#                       for k in xrange( -3,4 ) ):
#    pnts.add( a*r1.v1 + b*r1.v2 + c*r1.v3 )
#
#for p in v2.cut( pnts ):
#    p.draw( r=0.02 )

ps1 = set()
for a,b,c in ( (i,j,k) for i in xrange( -3,4 )\
                       for j in xrange( -3,4 )\
                       for k in xrange( -3,4 ) ):
    ps1.add( a*r1.v1 + b*r1.v2 + c*r1.v3 )

ps2 = set()
for a,b,c in ( (i,j,k) for i in xrange( -1,2 )\
                       for j in xrange( -1,2 )\
                       for k in xrange( -1,2 ) ):
    ps2.add( a*r2.v1 + b*r2.v2 + c*r2.v3 )

#for p in vo3.cut( ps1 ):
#    p.draw( r=0.02 )

for p in filter( vo3.touch, ps1 ) + filter( vo4.has, ps1 ):
    p.draw( r=0.02 )

for p in vo3.cut( list( ps2 ) ):
    print vo3.has( p )
    p.draw( r=0.04 )


draw_gl.app.start()

