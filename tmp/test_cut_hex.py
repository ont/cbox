#import psyco
#psyco.full()

import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

#(z( 0.0 0.0 0.0 -111.111 -111.111 -111.111 ), [  -2  -2   1 |  -2   1  -2 |   1  -2  -2 ])
#(r( 0.3 0.0 0.0 | 0.0 0.3 0.0 | 0.0 0.0 0.3 ), r( -0.6 -0.6 0.3 | -0.6 0.3 -0.6 | 0.3 -0.6 -0.6 ))

from vec   import *
from voron import *
from reper import *
from ucell import *
from spgrp import *

## drawing
from draw_gl  import drawgl
from draw_ipe import drawipe
import vec_gl
import geom_gl
import voron_gl

## converting
import vec2plane
import reper2dots
import ucell_min

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

    drawipe.clear()
    drawipe.setup_plane( pln, 10 )
    import math
    drawipe.th -= math.pi / 2
    drawipe( vhex )
    for p in vhex.has( ds1 ):
        drawipe( p, r=0.02, color = (0,1,0) )

    for p in vhex.has( ds2 ):
        drawipe( p, r=0.04, color = (1,0,0) )
    drawipe.save( '/tmp/sheme.ipe' )


ucm = None
def symm( *args ):
    global ucm
    uc = UCell( r_hex )
    uc.add( 'A', vhex.has( ds1 ) )
    uc.add( 'B', vhex.has( ds2 ) )
    ucm = uc.to_min()
    print uc
    print ucm

    r = ucm.rep
    r.v1 = -1 * r.v1
    print r.v3 * r.v1.vcross( r.v2 )
    f = open( '/tmp/basis_pcub_pcub.txt', 'w' )
    f.write( "rprim %s %s %s\n      %s %s %s\n      %s %s %s\n" % ( tuple( r[0] ) + tuple( r[1] ) + tuple( r[2] ) )  )
    f.write( '-----------\n' )
    for v in ucm.atoms['A']:
        f.write( "%s %s %s\n" % tuple( r.dec2frac( v ) ) )
        drawgl( v )

    f.write( '-----------\n' )
    for v in ucm.atoms['B']:
        f.write( "%s %s %s\n" % tuple( r.dec2frac( v ) ) )
        drawgl( v, r = 0.1, color = (1,0,0) )
    f.close()

    for v in ucm.rep:
        drawgl( v, style = 'line', color = (0,1,0) )
    #for l in open( '/tmp/spgrp.out', 'r' ).readlines():
    #    s = SpGrp( *map( int, l.split( ) ) )
    #    print s
    #    #for e in s:
    #        #print e


def view2ipe( *args ):
    import math
    drawipe.clear()

    for v in ucm.atoms['A']:
        drawipe( v )

    for v in ucm.atoms['B']:
        drawipe( v, r = 0.1, color = (1,0,0) )

    for v in ucm.rep:
        drawipe( v, style = 'line', color = (0,1,0) )

    drawipe.ortho = True
    drawipe.th   = drawgl.gl.theta * math.pi / 180
    drawipe.al   = drawgl.gl.alpha * math.pi / 180
    drawipe.dist = drawgl.gl.dist
    drawipe.save( '/tmp/sheme.ipe' )



def sel( obj ):
    global ucm
    if type( obj ) is Vec:
        s = SpGrp( 166, 2 )
        p = ucm.rep.dec2frac( obj )
        for v in s * p:
            v = ucm.rep * v
            drawgl( v, r = 0.05, color = (1,0,0) )


nelem = 0
def symmtest( *args ):
    basisA = ucm.rep.dec2frac( ucm.atoms['A'] )
    basisB = ucm.rep.dec2frac( ucm.atoms['B'] )
    print len( basisA )
    basisA = set( basisA )
    basisA.remove( Vec( 0.0, 0.0, 0.0 ) )
    print len( basisA )

    #for l in open( '/tmp/spgrp.out', 'r' ).readlines():
    for i in xrange( 1, 231 ):
        for j in xrange( 1, len( SpGrp.data[ i-1 ] ) + 1 ):
            #s = SpGrp( *map( int, l.split( ) ) )
            s = SpGrp( i, j )
            #print s

            f = True
            for p in basisA:
                for v in s * p:
                    if v not in basisA:
                        f = False
            if f:
                f = True
                for p in basisB:
                    for v in s * p:
                        if v not in basisB:
                            f = False
                if f:
                    print '---', s, 'YES'
            #else:
            #    print '---', s, 'no'


#def symmup( *args ):
#    global nelem
#    nelem += 1
#    if nelem >= len( s ):
#        nelem -= 1
#    symmdraw()
#
#def symmdown( *args ):
#    global nelem
#    nelem -= 1
#    if nelem < 0:
#        nelem += 1
#    symmdraw()




drawgl.button( 'up', up )
drawgl.button( 'down', down )
drawgl.button( 'fill', fill_hex )
drawgl.button( '2ipe', to_ipe )
drawgl.button( 'symm', symm )
drawgl.button( 'symmtest', symmtest )
drawgl.button( 'view2ipe', view2ipe )
#drawgl.button( 'symmup', symmup )
#drawgl.button( 'symmdown', symmdown )
drawgl.select( sel )

drawgl.start()
