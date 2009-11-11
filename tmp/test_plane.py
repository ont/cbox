#import psyco
#psyco.full()

import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from vec   import *
from voron import *
from spgrp import *
from reper import *

import draw_gl

import vec_gl
import geom_gl
import voron_gl
import vec2plane
import reper2dots
import geom_inout
import voron_inout

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

vo1 = Voron( *r1 )
vo2 = Voron( *r2 )
vo3 = Voron( *r3 )
vo4 = Voron( *r4 )

dots1 = r1.to_dots( 3,3,3 )
dots1 = vo3.cut( dots1 )

dots2 = r2.to_dots( 3,3,3 )
dots2 = vo3.cut( dots2 )

#for p in vo3.cut( dots ):
#    p.draw( r=0.01 )


v1 = -0.5 * ( r3[0] + r3[1] - r3[2] )
v2 = -1 * v1
#v1.draw( r=0.05 )
#v2.draw( r=0.05 )


plns = set()
for d in dots1:
    plns.add( v1.to_plane( d ) )
plns = list( plns )


#todraw = ( 7, )

todraw = ( 10, )

fd1 = r1.to_dots( 5,5,5 )
fd2 = r2.to_dots( 3,3,3 )




def draw( nc, n ):
    draw_gl.app.clear()

    vo3.draw()
    vo1.draw()

    for p in plns[ n ].touch( fd1 ):
        p.draw( r=0.02, color = (0,1,0) )

    for p in plns[ n ].touch( fd2 ):
        p.draw( r=0.04, color = (1,0,0) )



nl, n = None, 1

def up( *args ):
    global nl, n
    if n < len( plns ) - 1:
        nl,n = n, n+1
    draw( nl, n )

def down( *args ):
    global nl, n
    if n > 0:
        nl,n = n, n-1
    draw( nl, n )

draw_gl.app.button( 'up', up )
draw_gl.app.button( 'down', down )

draw_gl.app.start()
