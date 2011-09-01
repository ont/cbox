#!/usr/bin/env python2
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from strutils import *
from reper    import *
from spgrp    import *

import reper_coord

sg = None

argv = list( sys.argv )  ## copy list
argv.reverse()
if len( argv ) > 1:
    argv.pop()
    while argv:
        a = argv.pop()
        if a == '--spgrp':  ## make IT-tables basis
            n  = int( argv.pop() )
            ns = int( argv.pop() )
            sg = SpGrp( n, ns )


ls = list( stdlines() )
u = lines2cell( ls )


if sg:  ## need to minimize basis by space group
    res = {}
    for k,vv in u.atoms.iteritems():
        vv = u.rep.dec2frac( vv )
        vv = map( lambda v: v.z2o(), vv )
        vsym = set()
        for v in vv:
            vsym.update( sg * v )  ## add orbit to result set

        res[ k ] = u.rep.frac2dec( vsym )  ## assign to atom name new set of atoms

    u.atoms = res  ## full replace set of atoms

print cell2lines( u )
