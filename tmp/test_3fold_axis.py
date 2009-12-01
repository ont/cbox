import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from vec   import *
from voron import *
from reper import *
from ucell import *
from spgrp import *


v = Vec( 0.444444444444, 0.111111111111, 0.111111111111 )
vs = set( [ Vec( 0.444444444444, 0.111111111111, 0.111111111111 ),
            Vec( 0.111111111111, 0.111111111111, 0.444444444444 ),
            Vec( 0.111111111111, 0.444444444444, 0.111111111111 ) ] )

for i in xrange( 1, 231 ):
    for j in xrange( 1, len( SpGrp.data[ i-1 ] ) + 1 ):
        s = SpGrp( i, j )
        if set( s * v ) == vs:
            print s
        elif i == 146:
            print s * v
            for e in s:
                print e
            print s.cvecs()
