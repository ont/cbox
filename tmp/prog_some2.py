import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )


from vec   import *
from mat   import *
from zell  import *
from voron import *
from reper import *

import reper2zell
import zell2reper
import zell2sort

## drawing
import vec_gl
import voron_gl
from draw_gl import drawgl
from draw_ipe import drawipe

## build reper
p_l,p_n,p_m = 1.0,2.0,3.0
a = 2
b = (1 + 2 * p_m / p_l) * a
c = 3
v1 = Vec( -a/2.0, b/2.0, c/2.0 )
v2 = Vec(  a/2.0,-b/2.0, c/2.0 )
v3 = Vec(  a/2.0, b/2.0,-c/2.0 )
r = Reper( v1, v2, v3 )

## detect sort
s = r.to_zell().to_sort()
print 'sort of reper -', s

## build sublattice reper
sub_a = a / p_l
sub_c = c / ( p_l + 2 * p_n )
print 'v1 = ', v1
print 'v2 = ', v2
print 'v3 = ', v3
mv = Mat( *(list( v1 ) + list( v2 ) + list( v3 )) )
m  = Mat( b/2/sub_a + c/2/sub_c, -a/2/sub_a + c/2/sub_c, -a/2/sub_a + b/2/sub_a,
         -b/2/sub_a + c/2/sub_c,  a/2/sub_a + c/2/sub_c,  a/2/sub_a - b/2/sub_a,
          b/2/sub_a - c/2/sub_c,  a/2/sub_a - c/2/sub_c,  a/2/sub_a + b/2/sub_a )

m = m.inv()                                         ## invert matrix
print 'matrix of vectors (mv):', mv
print 'translational matrix (m):', m.inv()
print 'invert translational matrix (m.inv()):', m
print 'm.inv() * mv =', m * mv
sv1 =  Vec( *( m * mv )[ 0 ] )
sv2 =  Vec( *( m * mv )[ 1 ] )
sv3 =  Vec( *( m * mv )[ 2 ] )
print sv1
print sv2
print sv3
sr = Reper( sv1, sv2, sv3 )
print 'sort of sublattice -', sr.to_zell().to_sort()

## build & draw Voronoi polyhedra
print '-----------------'
print 'parameters a,b,c=', a,b,c
print 'parameter as=', sub_a
print 'translateional matrix:', m.inv()
print 'invert translateional matrix:', m
print 'lattice reper', r
print 'sublattice reper', sr
vo  = Voron( *r )
vos = Voron( *sr )
drawgl( vo )
drawgl( vos )
drawipe( vo )
drawipe( vos )

drawgl( sr[ 0 ], style = 'line' )
drawgl( sr[ 1 ], style = 'line' )
drawgl( sr[ 2 ], style = 'line' )


## button for output camera angles and distance
def pinfo( some ):
    print drawgl.gl.alpha, drawgl.gl.theta, drawgl.gl.dist
drawgl.button( 'camera info', pinfo )


## save picture to ipe file
import math
drawipe.setup( 24.0 * math.pi / 180, 128.0 * math.pi / 180, 27.207602388 )
#drawipe.setup( -13.0 * math.pi / 180, +65.0 * math.pi / 180, 15.559717968 )
drawipe.save( '/tmp/test4.ipe' )


drawgl.start()
