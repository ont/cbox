#!/usr/bin/env python2
import sys
import argparse
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from icsd import *

p = argparse.ArgumentParser( description = 'ICSD file dumper for dumping data to other tools (uctool, sginfo...)' )
p.add_argument( '-n', '--num', type = int, help = 'number of crystall from ICSD file to dump. You can skip this option to list crystalls' )
p.add_argument( '-s', '--spgrp', action = 'store_true', help = 'print space group' )
p.add_argument( '-r', '--reper', action = 'store_true', help = 'print crystall reper' )
p.add_argument( '-a', '--atoms', type = argparse.FileType('w'), help = 'file to dump out all crystall atoms line by line' )
p.add_argument( 'file', help = 'path to ICSD file to dump' )

args = p.parse_args()

if args.num is None:
    for i,c in enumerate( ICSD( args.file ) ):
        print '#%s' % i
        print c
    exit( 0 )
else:
    c = filter( lambda t: t[ 0 ] == args.num, enumerate( ICSD( args.file ) ) )[ 0 ][ 1 ]
    print '#ICSD:', c.icsd
    print c

    if args.reper:
        r = c.ucell.rep
        data = [ r.v1.x, r.v1.y, r.v1.z, 
                 r.v2.x, r.v2.y, r.v2.z,
                 r.v3.x, r.v3.y, r.v3.z ]
        data = map( lambda x: 0 if abs( x ) < 0.0001 else x, data )
        data = tuple( data )
        print '%s %s %s %s %s %s %s %s %s' % data

    if args.spgrp:
        print '%s,%s' % ( c.spgrp.num, c.spgrp.snum )

    if args.atoms:
        for n, ats in c.ucell:
            for a in ats:
                args.atoms.write( '%s %s %s %s\n' % ( n, a.x, a.y, a.z ) )
