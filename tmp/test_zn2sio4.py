import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from vec   import *
from reper import *
from math  import pi
from voron import *

from draw_gl import drawgl
import vec_gl
import vec_z2o
import reper_abc
import reper_coord
#import geom_gl
import voron_gl
import voron_inout

from spgrp import *

#-------------------------------------
d1 =  ( Vec( -1.75175, 1.100099, -0.808 ) -\
        Vec( -3.426423, 2.1574553, -0.8894464 ) ).vlen()
print "d1 =", d1

d2 = ( Vec( -1.3460447, -0.077077, -2.3425536 ) -\
       Vec( 0.0, 0.0, -3.232 ) ).vlen()
print "d2 =", d2


d2_1 = (Vec( 3.426423, -1.3460447, 2.5054464 ) -\
        Vec( 3.5035, 4.4408920985e-16, 1.616 ) ).vlen()
print "d2_1 =", d2_1

d3 = ( Vec( -1.75175, 1.100099, -0.808 ) -\
       Vec( -2.1574553, -0.077077, 0.7265536 ) ).vlen()
print "d3 = ", d3
#-------------------------------------

r = Reper.from_abc( 7.007, 7.007, 6.464, pi/2, pi/2, pi/2 )
c = ( r[0] + r[1] + r[2] ) * 0.5

vo = Voron( *r )
drawgl( vo )


s = SpGrp( 122, 1 )
print s.mydata
si = s * Vec( 0.0, 0.0, 0.5 )
zn = s * Vec( 0.157, 0.25, 0.125 )
o  = s * Vec( 0.3079, 0.489, 0.1376 )

si = set( map( lambda v: v.z2o(), si ) )
zn = set( map( lambda v: v.z2o(), zn ) )
o  = set( map( lambda v: v.z2o(), o  ) )

si = vo.cut( map( lambda v: v-c, r.frac2dec( si ) ) )
zn = vo.cut( map( lambda v: v-c, r.frac2dec( zn ) ) )
o  = vo.cut( map( lambda v: v-c, r.frac2dec( o  ) ) )

#for v in vo.cut( map( lambda v: v-c, r.frac2dec( si ) ) ):
for v in si:
    drawgl( v, r=0.1, color=(1,0,0) )

for v in zn:
    drawgl( v, r=0.1, color=(0,1,0) )

for v in o:
    drawgl( v, r=0.1, color=(0,0,1) )


def sel( obj ):
    if type( obj ) is Vec:
        print obj


def w_zn( *args ):
    drawgl.clear()
    drawgl( vo )
    for v in zn:
        drawgl( v )
        for vv in o:
            if abs( (v - vv).vlen() - d1 ) < 0.1:
                drawgl( Vec( *vv ), style='line', start=v )
                drawgl( Vec( *vv ), r=0.1, color=(0,0,1) )

def w_si( *args ):
    drawgl.clear()
    drawgl( vo )
    for v in si:
        drawgl( v )
        for vv in o:
            if abs( (v - vv).vlen() - d2 ) < 0.1:
                drawgl( Vec( *vv ), style='line', start=v )
                drawgl( Vec( *vv ), r=0.1, color=(0,0,1) )

drawgl.select( sel )
drawgl.button( 'w_zn', w_zn )
drawgl.button( 'w_si', w_si )

drawgl.start()

