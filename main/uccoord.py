#!/usr/bin/env python
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from strutils import *
from reper    import *
import reper_coord

ffrac  = False
fdec   = False

argv = list( sys.argv )  ## copy list
argv.reverse()
if len( argv ) > 1:
    argv.pop()
    while argv:
        a = argv.pop()
        if a == '--2frac':
            ffrac = True
        if a == '--2dec':
            fdec = True

ls = list( stdlines() )
u = lines2cell( ls )


for k,vs in u.atoms.iteritems():
    if ffrac and not fdec:
        u.atoms[ k ] = u.rep.dec2frac( vs )
    if fdec and not ffrac:
        u.atoms[ k ] = u.rep.frac2dec( vs )

print cell2lines( u )
