#!/usr/bin/env python2
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from strutils   import *
from spgrp      import *

from spgrp_gens import *



ls = list( stdlines() )
u = lines2cell( ls )

n  = sys.argv[ 1 ]
ns = sys.argv[ 2 ]
s  = SpGrp( i, j )

for i in xrange( 1, 231 ):
    for j in SpGrp.subs( i ):
        s = SpGrp( i, j )
        print i,j, len( s.full() )

