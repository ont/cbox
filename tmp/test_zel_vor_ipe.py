import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from draw_gl import drawgl

from   vec   import *
from   mat   import *
from   zell  import *
from   reper import *
from   voron import *

import voron_gl     ## aspect
import zell2reper   ## aspect

from spgrp import *


a = -2
b = -4
z = Zell( a, 0, a, a, b, a )
r = z.to_reper()
print r

vo = Voron( *r )
drawgl( vo )
drawgl.start()
exit( )
#r = Reper( Vec( 2.0, 2.0, 0.0 ),
#           Vec( 2.0, 0.0, 2.0 ),
#           Vec( 0.0, 2.0, 2.0 ) )
from math import *

## Cubic
r = Reper.from_abc( 1, 1, 1, pi/2, pi/2, pi/2 )

### Hexagonal
#alf = 120 * pi / 180.0
#r = Reper( Vec( 1.0, 0.0, 0.0 ),
#           Vec( cos(alf), sin(alf), 0.0 ),
#           Vec( 0.0, 0.0, 3.0 ) )
#
### Triclinical
#r = Reper.from_abc( 1, 2, 3, pi/3, pi/4, pi/5 )
#
### Monoclinic
#r = Reper.from_abc( 1, 2, 3, pi/2, pi/2, pi/5 )
#
### Orthorombic
#r = Reper.from_abc( 1, 2, 3, pi/2, pi/2, pi/2 )
#
### Rombohedral (trigonal)
#r = Reper.from_abc( 1, 1, 1, pi/3.3, pi/3.3, pi/3.3 )
#
### Tetragonal
#r = Reper.from_abc( 1, 1, 3, pi/2, pi/2, pi/2 )



print r

m = Mat( *(list( r.v1 ) + list( r.v2 ) + list( r.v3 )) )
m = m.t()
mi = m.inv()
print m, mi




def test( n, sn ):
    s = SpGrp( n, sn )
    f = True
    for e in s:
        ah = e[ 0 ]
        a  = m * ah * mi
        #print '--------'
        #print 'ah = ', ah
        #print 'a  =',  a
        #print a * a.t()
        #print a.is_ortho()
        if not a.is_ortho():
            f = False
            break

    return f


#print len( SpGrp.data[ 75 - 1 ] )
#test( 225, 1 )


s = set()
f = open( '/tmp/spgrp.out', 'w' )
for i in xrange( 1, 231 ):
    for j in xrange( 1, len( SpGrp.data[ i-1 ] ) + 1 ):
        if test( i, j ):
            s.add( i )
            f.write( "%s %s\n" % (i,j) )
            print ( i, j ),
f.close()

print
print "set() - set() =", set( range( 1, 231 ) ) - s

l = list( s )
l.sort()
print '----', l
#print '----', range( 1, 143 )
