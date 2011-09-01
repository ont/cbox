#!/usr/bin/env python2
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from strutils import *
from reper    import *
from voron    import *
from spgrp    import *
from vec      import *

import vec_z2o
import ucell_min
import reper2zell
import reper_min
import reper_coord
import zell2sort
import voron_inout


fbasis = False
fmin   = False
ffrac  = False
fz2o   = False
fvoron = False
sg     = None

argv = list( sys.argv )  ## copy list
argv.reverse()
if len( argv ) > 1:
    argv.pop()
    while argv:
        a = argv.pop()
        if a == '--IT':  ## make IT-tables basis
            fbasis = True
        elif a == '--min':
            fmin   = True
        elif a == '--frac':
            ffrac  = True
        elif a == '--z2o':
            fz2o   = True
        elif a == '--voron':
            fz2o   = True  ## always cut by unit cell befor Voronoi
            fvoron = True
        elif a == '--spgrp':
            n  = int( argv.pop() )
            ns = int( argv.pop() )
            sg = SpGrp( n, ns )



ls = list( stdlines() )
u = lines2cell( ls )

if ffrac:  ## convert to decart basis
    res = {}
    for k,vv in u.atoms.iteritems():
        res[ k ] = u.rep.frac2dec( vv )
    u.atoms = res


if fz2o:
    res = {}
    for k,vv in u.atoms.iteritems():
        res[ k ] = set( map( lambda v: v.z2o(), u.rep.dec2frac( vv ) ) )
        res[ k ] = u.rep.frac2dec( res[ k ] )
    u.atoms = res


if fvoron:
    u = u * 1  ## expand in all directions by 1
    vo = Voron( *u.rep )
    for k,v in u.atoms.iteritems():
        u.atoms[ k ] = vo.has( v )


if fmin:
    u = u.to_min()


if fbasis:
    s =  u.rep.to_zell().to_sort()

    ## TODO: need code for 'K3'
    if s.name == 'K1':
        r =  u.rep.minimize()
        if r.v1 * r.v2 > 0:
            r.v1 *= -1

        a = r.v2 - r.v1
        v1n = 2 * r.v2 - a

        if r.v2 * r.v3 > 0:
            r.v3 *= -1

        a = r.v3 - r.v2
        v2n = v1n + a

        v3n = ( v1n.vcross( v2n ).norm() ) * v1n.vlen()


        u = u * 1  ## extend in all directions by 1

        u.rep.v1 = v1n
        u.rep.v2 = v2n
        u.rep.v3 = v3n

        vo = Voron( v1n, v2n, v3n )
        for k,v in u.atoms.iteritems():
            u.atoms[ k ] = vo.has( v )


if sg:  ## need to minimize basis by space group
    res = {}
    for k,vv in u.atoms.iteritems():
        vv = u.rep.dec2frac( vv )
        vv = map( lambda v: v.z2o(), vv )
        for v in vv:
            vs = sg * v
            vs.remove( v )  ## do not delete this atom
            for dv in vs:   ## delete each vector from this set
                if dv not in vv:
                    print '--v->', v
                    print 'sg*v>', vs
                    print 'notf>', dv
                    print '-vv->', vv
                    raise Exception, 'Wrong space group for unit cell'
                vv.remove( dv )
                #print '---->', dv

        ## now move atoms from basis more closer to origin
        vvm = []
        for v in vv:
            vs = sg * v  ## take orbit of this point
            vs = u.rep.frac2dec( vs ) ## convert to decart coordinate system
            vs.sort( key = lambda vt: vt.vlen() )  ## sort by distance
            vvm.append( vs[ 0 ] )                  ## ... and take nearest


        res[ k ] = vvm  ## assign to atom name new set of atoms

    u.atoms = res  ## full replace set of atoms

print cell2lines( u )
