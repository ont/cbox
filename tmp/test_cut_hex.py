import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

#(z( 0.0 0.0 0.0 -111.111 -111.111 -111.111 ), [  -2  -2   1 |  -2   1  -2 |   1  -2  -2 ])
#(r( 0.3 0.0 0.0 | 0.0 0.3 0.0 | 0.0 0.0 0.3 ), r( -0.6 -0.6 0.3 | -0.6 0.3 -0.6 | 0.3 -0.6 -0.6 ))

from vec   import *
from voron import *
from reper import *

## drawing
import draw_gl
import vec_gl
import geom_gl
import voron_gl

## converting
import vec2plane
import reper2dots

## filtering
import geom_inout
import voron_inout


r1 = Reper( Vec( 0.3, 0.0, 0.0 ),
            Vec( 0.0, 0.3, 0.0 ),
            Vec( 0.0, 0.0, 0.3 ) )

r2 = Reper( Vec( -0.6, -0.6,  0.3 ),
            Vec( -0.6,  0.3, -0.6 ),
            Vec(  0.3, -0.6, -0.6 ) )


vo1   = Voron( *r1 )
vo2   = Voron( *r2 )
vo21  = Voron( r2[0], r2[1], r2[2], pos = Vec( -0.45, -0.45, -0.45 ) )
vo22  = Voron( r2[0], r2[1], r2[2], pos = Vec(  0.45,  0.45,  0.45 ) )

vo1.draw()
vo2.draw()

n = ( 0.5*r2[0] + 0.5*r2[1] + 0.5*r2[2] ).norm()  ## normal to plane

## creating set of dots
ds1 = r1.to_dots( 5,5,5 )
ds2 = r2.to_dots( 3,3,3 )

plns = set()
for d in vo2.cut( ds1 ):
    plns.add( n.to_plane( d ) )
plns = list( plns )


r0 = plns[ 0 ].r
dr = r0 - plns[ 1 ].r
num = 0


v_h1 = Vec( 0.0, 0.9, -0.9 )
v_h2 = Vec( 0.9, 0.0, -0.9 )
r_hex = Reper( v_h1,
               v_h2,
               v_h1.vcross( v_h2 ).norm() * Vec( 0.9, 0.9, 0.9 ).vlen() * 2 )
vhex = Voron( *r_hex )

def draw():
    print num
    draw_gl.app.clear()

    vo1.draw()
    vo2.draw()
    vhex.draw()

    pln = n.to_plane( r0 + num * dr )
    for p in pln.touch( ds1 ):
        p.draw( r=0.02, color = (0,1,0) )

    for p in pln.touch( ds2 ):
        p.draw( r=0.04, color = (1,0,0) )


def up( *args ):
    global num
    num -= 1
    draw()

def down( *args ):
    global num
    num += 1
    draw()

def sel( obj ):
    print obj


def fill_hex( *args ):
    print args
    draw_gl.app.clear()

    vo1.draw()
    vo21.draw()
    vo22.draw()
    vhex.draw()

    #for i in xrange( -20, 20 ):
    #    pln = n.to_plane( r0 + i * dr )
    #    if pln.touch( ds2 ):
    #        ps1 = pln.touch( ds1 )
    #        ps2 = pln.touch( ds2 )

    #        for p in vhex.has( ps1 ):
    #            p.draw( r=0.02, color = (0,1,0) )

    #        for p in vhex.has( ps2 ):
    #            p.draw( r=0.04, color = (1,0,0) )


    for p in vhex.has( ds1 ):
        p.draw( r=0.02, color = (0,1,0) )

    for p in vhex.has( ds2 ):
        p.draw( r=0.04, color = (1,0,0) )


draw_gl.app.button( 'up', up )
draw_gl.app.button( 'down', down )
draw_gl.app.button( 'fill', fill_hex )
draw_gl.app.select( sel )

draw_gl.app.start()
