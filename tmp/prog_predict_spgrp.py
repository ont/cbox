import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from spgrp import *
import spgrp_gens

for n in xrange( 1, 231 ):
    print n
    for ns in SpGrp.subs( n ):
        s = SpGrp( n, ns )
        ops = s.full()
        mats = map( lambda t: t[ 0 ], ops )
        #if len( ops ) == 4 and filter( lambda x: x[ 0 ] == Mat( -1,0,0, 0,-1,0, 0,0,-1 ), ops ):
        #    print s
            
        m1 = ( Mat( -1,0,0, 0,-1,0, 0,0, 1 ), Vec( 0, 0.5, 0.5 ) )
        m2 = ( Mat(  1,0,0, 0, 1,0, 0,0,-1 ), Vec( 0, 0.5, 0.5 ) )
        m3 = ( Mat( -1,0,0, 0,-1,0, 0,0,-1 ), Vec( 0, 0, 0 ) )
        if len( ops ) == 4 and m1 in ops and m2 in ops and m3 in ops:
            print s
