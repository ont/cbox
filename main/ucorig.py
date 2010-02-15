#!/usr/bin/env python
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from strutils import *
from vec      import *
import vec_z2o
import reper_coord


opos = Vec( 0.0, 0.0, 0.0 )  ## new origin position

argv = list( sys.argv )  ## copy list
argv.reverse()
if len( argv ) > 1:
    argv.pop()
    while argv:
        a = argv.pop()
        if a == '--to':  ## make IT-tables basis
            x = float( argv.pop() )
            y = float( argv.pop() )
            z = float( argv.pop() )
            opos = Vec( x,y,z )


ls = list( stdlines() )
u = lines2cell( ls )

for k,vv in u.atoms.iteritems():
    vv = u.rep.dec2frac( vv )
    vv = map( lambda v: ( v - opos ).z2o(), vv )
    vv = u.rep.frac2dec( vv )
    u.atoms[ k ] = vv

print cell2lines( u )
