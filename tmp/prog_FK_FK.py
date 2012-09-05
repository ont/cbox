import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )


from vec   import *
from voron import *
from reper import *
from ucell import *
from spgrp import *

import vec2plane
import reper2dots
import geom_inout
import voron_inout
import ucell_min
import vec_z2o

## drawing
from draw_gl import drawgl
from draw_ipe import drawipe
import vec_gl
import geom_gl
import voron_gl



## -------- starting data
r1 = Reper( Vec( 1.41421356237, 0, 0 ),
            Vec( -0.707106781187, 1.22474487139, 0 ),
            Vec( 0.0, -0.816496580928, 1.15470053838 ) ) 

r2 = Reper( Vec( -2.12132034356, -3.67423461417, 0.0 ),
            Vec( -2.12132034356, 3.67423461417, 0.0 ),
            Vec( 2.12132034356, -1.22474487139, 3.46410161514 ) )

vo1 = Voron( *r1 )
vo2 = Voron( *r2 )

ds1 = r1.to_dots( 10,10,10 )
ds2 = r2.to_dots( 4,4,4 )


## -------- after selecting
vc = Vec( 0.0, 0.0, 0.0 )
v1 = Vec( -3.99991151312e-12, 2.44948974278, 0.0 )
v2 = Vec( -2.12132034356, 1.22474487139, 0.0 )
v3 = Vec( 2.12132034355, 1.22474487139, 0.0 )

va = v1 + v2
vb = v1 + v3
#vc = v2.vcross( v1 )
vc = Vec( 0, 0, 10.3923048454 )

#drawgl( v1, style='line' )
#drawgl( v2, style='line' )
#drawgl( v3, style='line' )

drawgl( va, style='line' )
drawgl( vb, style='line' )
drawgl( vc, style='line' )
#drawgl( -1 * vc, style='line' )

vo_h   = Voron( va, vb, vc )
vo_h_m = Voron( va, vb, vc, pos = vc )
drawgl( vo_h   )
drawgl( vo_h_m )


## -------- cut dots
ds1_h = vo_h.has( ds1 ) + vo_h_m.has( ds1 )
ds2_h = vo_h.has( ds2 ) + vo_h_m.has( ds2 )

## -------- calculating deltas for planes
pos = 0  ## global position in deltas array
deltas = set( map( lambda x: x.vdot( vc.norm() ), ds1_h ) )
deltas = list( deltas )
deltas.sort()
delta = abs( deltas[ 0 ] - deltas[ 1 ] )

## -------- drawing
for p in ds1_h:
    drawgl( p, r = 0.10, color=(0,1,0) )

for p in ds2_h:
    drawgl( p, r = 0.11, color=(1,0,0) )
#drawgl( vo1 )
#drawgl( vo2 )


def select( obj ):
    if type( obj ) == Vec:
        print obj



def redraw():
    global vc, pos, delta
    v = vc.norm() * delta * pos
    p = vc.to_plane( v )
    drawgl.clear()
    drawgl( vo_h )
    drawgl( p )
    for x in p.touch( ds1_h ):
        drawgl( x, r = 0.10, color=(0,1,0) )

    for x in p.touch( ds2_h ):
        drawgl( x, r = 0.11, color=(1,0,0) )


def to_ipe( *args ):
    global vc, pos, delta
    v = vc.norm() * delta * pos
    p = vc.to_plane( v )

    drawipe.group()  ## make new group
    drawipe( vo_h )
    drawipe.setup_plane( p, 10 )

    for x in p.touch( ds1_h ):
        drawipe( x, r=0.04, color=(1,0,0) )

    for x in p.touch( ds2_h ):
        drawipe( x, color=(0,1,0) )

def to_ipe2( *args ):
    global va
    v = va.norm()
    p = v.to_plane( va )

    drawipe.group()  ## make new group
    drawipe( vo_h )
    drawipe.setup_plane( p, 10 )

    for x in vo_h.has( ds1_h ):
        drawipe( x, r=0.04, color=(1,0,0) )

    for x in vo_h.has( ds2_h ):
        drawipe( x, color=(0,1,0) )


def ipe2file( *args ):
    drawipe.save( '/tmp/test.ipe' )
    drawipe.clear()


def bnext( *args ):
    global pos
    pos += 1
    redraw()


def bprev( *args ):
    global pos
    pos -= 1
    redraw()


drawgl.button( "next", bnext )
drawgl.button( "prev", bprev )
drawgl.button( "toipe", to_ipe )
drawgl.button( "toipe2", to_ipe2 )
drawgl.button( "ipe2file", ipe2file )
drawgl.select( select )
drawgl.start()
