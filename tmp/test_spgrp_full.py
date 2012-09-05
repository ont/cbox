import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from spgrp import *

import spgrp_gens


s = SpGrp( 6, 1 )
print 'gens --->', s.gens
print 'list --->', list( s )
print 'full ---->', s.full()

s = SpGrp( 167, 1 )
print 'gens --->', s.gens
print 'list --->', list( s )
print 'full ---->', s.full()
