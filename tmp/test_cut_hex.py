import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

#(z( 0.0 0.0 0.0 -111.111 -111.111 -111.111 ), [  -2  -2   1 |  -2   1  -2 |   1  -2  -2 ])
#(r( 0.3 0.0 0.0 | 0.0 0.3 0.0 | 0.0 0.0 0.3 ), r( -0.6 -0.6 0.3 | -0.6 0.3 -0.6 | 0.3 -0.6 -0.6 ))

from vec   import *
from voron import *
from reper import *

## drawing
from draw_gl import drawgl
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

drawgl( vo1 )
drawgl( vo2 )

n = ( 0.5*r2[0] + 0.5*r2[1] + 0.5*r2[2] ).norm()  ## normal to plane

## creating set of dots
ds1 = r1.to_dots( 5,5,5 )
ds2 = r2.to_dots( 3,3,3 )

plns = set()
for d in vo2.cut( ds1 ):
    plns.add( n.to_plane( d ) )
plns = list( plns )



np = min( plns[ 1: ],
          key= lambda p: ( plns[ 0 ].r - p.r ).vlen() )  ## find nearest plane (np)
r0 = plns[ 0 ].r
dr = plns[ 0 ].r - np.r
num = 0


v_h1 = Vec( 0.0, 0.9, -0.9 )
v_h2 = Vec( 0.9, 0.0, -0.9 )
r_hex = Reper( v_h1,
               v_h2,
               v_h1.vcross( v_h2 ).norm() * Vec( 0.9, 0.9, 0.9 ).vlen() )

pos = 0.5 * ( Vec( 0.6, 0.6, -0.3 ) +\
              Vec( -0.3, 0.6, 0.6 ) +\
              Vec( 0.6, -0.3, 0.6 ) )
vhex = Voron( r_hex.v1, r_hex.v2, r_hex.v3, pos = pos )

def draw():
    print num
    drawgl.clear()

    #drawgl( vo1 )
    #drawgl( vo2 )
    drawgl( vhex )

    pln = n.to_plane( r0 + num * dr )
    for p in pln.touch( vhex.has( ds1 ) ):
        drawgl( p, r=0.02, color = (0,1,0) )

    for p in pln.touch( vhex.has( ds2 ) ):
        drawgl( p, r=0.04, color = (1,0,0) )


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
    drawgl.clear()

    drawgl( vo1  )
    drawgl( vo21 )
    drawgl( vo22 )
    drawgl( vhex )

    for p in vhex.has( ds1 ):
        drawgl( p, r=0.02, color = (0,1,0) )

    for p in vhex.has( ds2 ):
        drawgl( p, r=0.04, color = (1,0,0) )


def to_ipe( *args ):
    #global num, r0, dr
    from draw_ipe import drawipe

    for num in xrange( -9, 1 ):
        drawipe.clear()
        pln = n.to_plane( r0 + num * dr )
        drawipe.setup_plane( pln, 10 )

        for p in pln.touch( vhex.has( ds1 ) ):
            drawipe( p, r=0.02, color = (0,1,0) )

        for p in pln.touch( vhex.has( ds2 ) ):
            drawipe( p, r=0.04, color = (1,0,0) )

        drawipe( vhex )
        #drawipe( vo21 )
        #drawipe( vo22 )
        drawipe.save( '/tmp/%s.ipe' % abs( num ) )


drawgl.button( 'up', up )
drawgl.button( 'down', down )
drawgl.button( 'fill', fill_hex )
drawgl.button( '2ipe', to_ipe )
drawgl.select( sel )

drawgl.start()
