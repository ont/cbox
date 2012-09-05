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

from draw_gl  import drawgl
from draw_ipe import drawipe
import vec_gl
import geom_gl
import voron_gl

## -------- starting data
r1 = Reper( Vec(  0.3,  0.0,             0.0 ),
            Vec( -0.1,  0.282842712475,  0.0 ),
            Vec( -0.1, -0.141421356237,  0.244948974278 ) )

r2 = Reper( Vec( -0.5, -0.707106781187,  0.244948974278 ),
            Vec( -0.5,  0.565685424949, -0.489897948557 ),
            Vec(  0.7, -0.282842712475, -0.489897948557 ) )

vo1 = Voron( *r1 )
vo2 = Voron( *r2 )


ds1 = r1.to_dots( 7,7,7 )
ds2 = r2.to_dots( 4,4,4 )



## -------- after selecting

## cube
v1 = Vec( -0.2 , 0.989949493662  , 0.244948974279 )
v2 = Vec( 1.0  , 0.141421356238  , 0.244948974279 )
v3 = Vec( -0.2 , -0.282842712474 , 0.979795897114 )
vc = 1/3 * ( v1 + v2 + v3 )
v1,v2,v3 = v1 - vc, v2 - vc, ( v1 -vc ).vcross( v2 - vc )


## hexagonal prism
v1 = Vec( -0.5, -0.707106781187,  0.244948974278 )
v2 = Vec( -0.5,  0.565685424949, -0.489897948556 )
v3 = Vec(  0.7, -0.282842712476, -0.489897948556 )

ve1 = Vec( 0.8, -0.141421356235,  1.22474487139  )
ve2 = Vec( 0.2, -0.989949493663, -0.244948974278 )

vc = 1/3.0 * ( v1 + v2 + v3 )
v1,v2 = v1 - vc, v2 - vc
v3 = (ve1 - ve2).vlen() * v1.vcross( v2 ).norm()
v1,v2 = v1+v2+v1, v1+v2+v2

r3 = Reper( v1, v2, v3 )
vo3 = Voron( *r3 )

#for p in r3.to_dots( 2, 2, 2 ):
#    drawgl( p, r=0.05, color=(0,1,0) )


## ----------- planes for cutting
edg = ve1 - ve2
pln = ( 0.5 * edg ).to_plane( 0.5 * edg )
drawgl( pln )

pln.do_norm()
drs = map( lambda p: ( pln.r - p ) * pln.n, vo3.has( ds1 ) )
drs = filter( lambda d: abs( d ) > 0.0001, drs )
dr  = min( drs )
print dr



## ----------- drawing
f = open( '/home/ont/make_it/kem/cbox/tmp/ock.txt', 'a' )
for p in vo3.has( ds1 ):
    drawgl( p, color=(0,1,0) )
    f.write( 'A %s %s %s\n' % tuple( p ) )

for p in vo3.has( ds2 ):
    drawgl( p, r=0.04, color=(1,0,0) )
    f.write( 'B %s %s %s\n' % tuple( p ) )

drawgl( vo1 )
drawgl( vo2 )
drawgl( vo3 )

drawgl( edg, style="line" )


def select( obj ):
    if type( obj ) == Vec:
        print obj


## -------- functions for cutting
n = 0
def draw( n ):
    drawgl.clear()
    drawgl( vo3 )

    vn = edg.norm()
    pln = vn.to_plane( vn * dr * n )
    drawgl( pln )

    for p in pln.touch( vo3.has( ds1 ) ):
        drawgl( p, color=(0,1,0) )

    for p in pln.touch( vo3.has( ds2 ) ):
        drawgl( p, r=0.04, color=(1,0,0) )



def to_ipe( *args ):
    drawipe.group()  ## make new group
    drawipe( vo3 )
    vn = edg.norm()
    pln = vn.to_plane( vn * dr * n )
    drawipe.setup_plane( pln, 10 )

    for p in pln.touch( vo3.has( ds1 ) ):
        drawipe( p, color=(0,1,0) )

    for p in pln.touch( vo3.has( ds2 ) ):
        drawipe( p, r=0.04, color=(1,0,0) )


def to_ipe2( *args ):
    v = vo3.rep[0] + vo3.rep[1]
    v = v.norm()
    pln = v.to_plane( v * 2 )

    drawgl( v * 2, style="line" )

    drawipe.setup_plane( pln, 10 )

    for p in vo3.has( ds1 ):
        drawipe( p, color=(0,1,0) )

    for p in vo3.has( ds2 ):
        drawipe( p, r=0.04, color=(1,0,0) )

    drawipe( vo3 )


def ipe2file( *args ):
    drawipe.save( '/tmp/test.ipe' )
    drawipe.clear()


def up( *args ):
    global n
    n += 1
    draw( n )

def down( *args ):
    global n
    n -= 1
    draw( n )


def min_cell( *args ):
    uc = UCell( vo3.rep )
    uc.add( 'A', vo3.has( ds1 ) )
    uc.add( 'B', vo3.has( ds2 ) )
    print len( uc.pnts['A'] )
    print len( uc.pnts['B'] )
    uc = uc.to_min()
    print len( uc.pnts['A'] )
    print len( uc.pnts['B'] )

    #drawgl.clear()
    for v in uc.rep:
        drawgl( v, style="line" )

    f = open( '/tmp/basis_ock_ock.txt', 'w' )
    r = uc.rep
    print r.v3 * r.v1.vcross( r.v2 )
    f.write( "rprim %s %s %s\n      %s %s %s\n      %s %s %s\n" % ( tuple( r[0] ) + tuple( r[1] ) + tuple( r[2] ) )  )

    f.write( '-----------\n' )
    for v in uc.pnts['A']:
        f.write( "%s %s %s\n" % tuple( r.dec2frac( v ) ) )
        drawgl( v, r=0.04, color=(0,0,1) )

    f.write( '-----------\n' )
    for v in uc.pnts['B']:
        f.write( "%s %s %s\n" % tuple( r.dec2frac( v ) ) )
        drawgl( v, r=0.06, color=(1,0,0) )

    f.close()


def cubic( *args ):

    ## old cube
    vc = Vec( -0.5, -0.707106781187, 0.244948974278 )
    v1 = Vec( -0.7, 0.282842712476, 0.489897948556 )
    v2 = Vec( -0.3, -0.424264068713, -0.734846922836 )
    v3 = Vec( 0.5, -0.565685424949, 0.489897948556 )
    v1,v2,v3 = v1 - vc, v2 - vc, v3 - vc


    ## new cube
    vc = Vec( 0.8, -0.141421356235, 1.22474487139 )
    v1 = Vec( -0.2, -0.282842712473, 0.979795897112 )
    v2 = Vec( 1.0, 0.141421356238, 0.244948974278 )
    v3 = Vec( 1.0, -1.1313708499, 0.979795897112 )
    v1,v2,v3 = v1 - vc, v2 - vc, v3 - vc

    drawgl.clear()


    ## -- draw cube
    vc = Voron( v1, v2, v3, pos = 0.5 * ( v1+v2+v3 ) )

    for v in vc.has( ds1 ):
        drawgl( v, color=(0,1,0) )

    for v in vc.has( ds2 ):
        drawgl( v, r=0.04, color=(1,0,0) )

    #drawgl( vc )
    drawgl( vo1 )
    drawgl( vo2 )


    basisA = vc.has( ds1 )
    basisA = vc.rep.dec2frac( basisA )
    basisA = map( lambda v: v.z2o(), basisA )
    basisB = [ Vec( 0.0, 0.0, 0.0 ),
               Vec( 0.5, 0.5, 0.5 ) ]

    basisA = set( basisA )
    basisB = set( basisB )

    print 'len( basisA ) = ', len( basisA )
    print 'len( basisB ) = ', len( basisB )

    basisA = basisA - basisB

    print 'len( basisA ) = ', len( basisA )
    print 'len( basisB ) = ', len( basisB )


    ## -- output basis to file
    f = open( '/tmp/basis_ock_ock.txt', 'w' )
    r = vc.rep
    print r.v3 * r.v1.vcross( r.v2 )

    f.write( "rprim   %s %s %s\n      %s %s %s\n      %s %s %s\n" % ( tuple( r[0] ) + tuple( r[1] ) + tuple( r[2] ) )  )
    f.write( "vc.rep\t%s\n\t\t%s\n\t\t%s\n" % ( vc.rep[ 0 ], vc.rep[ 1 ], vc.rep[ 2 ] ) )

    for v in ( vc.rep[ 0 ], vc.rep[ 1 ], vc.rep[ 2 ] ):
        drawgl( v, style = 'line' )

    f.write( '-----------\n' )
    for v in basisA:
        f.write( "%s %s %s\n" % tuple( v ) )

    f.write( '-----------\n' )
    for v in basisB:
        f.write( "%s %s %s\n" % tuple( v ) )

    f.close()


    ## -- test space groups
    for i in xrange( 1, 231 ):
        for j in SpGrp.subs( i ):
            s = SpGrp( i, j )

            f = True
            for p in basisA:
                for v in s * p:
                    if v not in basisA:
                        f = False
                        break
                if not f:
                    break

            if f:
                for p in basisB:
                    for v in s * p:
                        if v not in basisB:
                            f = False
                if f:
                    print '---', s, 'YES'

            #if f:
            #    print '---', s, 'YES'


    return 

    ## -- output other basis
    v1, v2, v3 = v1, v2, 0.5 * (v1 + v2 + v3)
    vc = Voron( v1, v2, v3 )
    drawgl( vc )

    f = open( '/tmp/basis_ock_ock2.txt', 'w' )
    r = vc.rep
    print r.v3 * r.v1.vcross( r.v2 )

    for v in r:
        drawgl( v, style="line", color=( 1,0,0 ) )

    basisA = vc.has( ds1 )
    basisA = vc.rep.dec2frac( basisA )
    basisA = map( lambda v: v.z2o(), basisA )
    basisB = [ Vec( 0.0, 0.0, 0.0 ) ]

    basisA = set( basisA )
    basisB = set( basisB )

    print 'len( basisA ) = ', len( basisA )
    print 'len( basisB ) = ', len( basisB )

    basisA = basisA - basisB

    print 'len( basisA ) = ', len( basisA )
    print 'len( basisB ) = ', len( basisB )


    f.write( "rprim %s %s %s\n      %s %s %s\n      %s %s %s\n" % ( tuple( r[0] ) + tuple( r[1] ) + tuple( r[2] ) )  )

    f.write( '-----------\n' )
    for v in basisA:
        f.write( "%s %s %s\n" % tuple( v ) )
        drawgl( r.frac2dec( v ), r=0.05, color = (0,0,1) )

    f.write( '-----------\n' )
    for v in basisB:
        f.write( "%s %s %s\n" % tuple( v ) )
        drawgl( r.frac2dec( v ), r=0.05, color = (0,1,1) )

    f.close()



drawgl.button( "up"  , up   )
drawgl.button( "down", down )
drawgl.button( "toipe", to_ipe )
drawgl.button( "toipe2", to_ipe2 )
drawgl.button( "ipe2file", ipe2file )
drawgl.button( "mincell", min_cell )
drawgl.button( "cubic", cubic )
drawgl.select( select )
drawgl.start()
