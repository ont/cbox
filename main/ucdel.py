#!/usr/bin/env python2
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from strutils import *

ls = list( stdlines() )
u = lines2cell( ls )

for n in sys.argv[ 1: ]:
    for nt, vs in u.atoms.iteritems():
        if nt != n:
            u.atoms[ n ] -= vs

print cell2lines( u )
