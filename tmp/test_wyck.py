import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from   spgrp      import *
import spgrp_wyck

s = SpGrp( 2, 1 )
print SpGrp.data[ 2-1 ][ 0 ]
for i, w in enumerate( s.wyckiter() ):
    print w
    if i == 10:
        break

#print "---------"

#for e in s:
#    print e

#print "---------"

v = Vec( 0.5, 0.5, 0.0 )
a = Vec( 0.5, 0.5, 0.0 )
b = Vec( 0.5, 0.0, 0.5 )
c = Vec( 0.0, 0.5, 0.5 )
for x in xrange( 2 ):
    for y in xrange( 2 ):
        for z in xrange( 2 ):
            print v + x * a + y * b + z * c, x, y, z


from reper import *
import reper_min
r = Reper( Vec( 8, 1, 0 ),
           Vec( 1, 0, 0 ),
           Vec( 0, 0, 1 ) )
print r
print r.minimize()


#import spgrp_gens
#s = SpGrp( 225, 1 )
#gs = [ (Mat( 0,1,0, 1,0,0, 0,0,-1 ), Vec( 0,0,0 ) ) ]
#print s.gens2set( gs )
