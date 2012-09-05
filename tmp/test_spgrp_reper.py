import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from spgrp import *
from reper import *
from mat   import *
from vec   import *
from math  import *

import mat_ortho
import reper_abc



#v1 = Vec( 1.0  , 0.0  , 0.0 )
#v2 = Vec( 0.0  , 1.0  , 0.0 )
#v3 = Vec( 0.5  , 0.5  , 0.5 )

v1 = Vec( 1.0  , 0.0  , 0.0 )
v2 = Vec( 0.0  , 1.0  , 0.0 )
v3 = Vec( 0.0  , 0.0  , 2.0 )

r = Reper.from_abc( 3,3,3, pi / 3, pi / 3, pi / 3 )
print r

b = Mat( *( list( r.v1 ) + list( r.v2 ) + list( r.v3 ) ) )
b  = b.t()
bi = b.inv()

print b, bi

for n in xrange( 1, 231 ):
    for ns in SpGrp.subs( n ):
        s = SpGrp( n, ns )

        f = True
        for e in s:
            if not ( b * e[ 0 ] * bi ).is_ortho():
                f = False
                break

        if f:
            print '##%s, %s##' % ( s.num, s.snum ),
        else:
            print '%s, %s' % ( s.num, s.snum ),
