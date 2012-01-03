#!/usr/bin/env python2
import sys
import argparse
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from spgrp import *
import spgrp_wyck

p = argparse.ArgumentParser( description = 'Spage group information retriever' )
p.add_argument( '--sym', metavar = 'NAME', help = 'view info by space group name (for example  "F m -3 m")' )
p.add_argument( 'num'  , type=int, nargs = '?', default = None, help = 'main number of space group' )
p.add_argument( 'snum' , type=int, nargs = '?', default = None, help = 'origin and orientation choice number' )

args = p.parse_args()
if not args.num and not args.snum and not args.sym:
    p.print_usage()
    exit( 1 )

def info( s ):
    print '--------------[basic   ]--------------'
    print s
    print 'additional non-lattice translational vectors:', s.cvecs()
    print 'count of generators:', len( s )
    for i,o in enumerate( s ):
        print '---- generator #%s:' % i,
        print o[ 0 ], o[ 1 ], '\n'
    print '--------------[metadata]--------------'
    print s.mydata
    print '--------------[wyck pos]--------------'
    for ws in s.wyckpos():
        print ws

if args.snum:
    s = SpGrp( args.num, args.snum )
    info( s )

elif args.num:
    for sn,g in enumerate( SpGrp.data[ args.num-1 ] ):
        print 'origin/orientation (%s) -- %s' % ( sn + 1, g['symb'] )

elif args.sym:
    for n,gs in enumerate( SpGrp.data ):
        for sn,g in enumerate( gs ):
            if g['symb'] == args.sym:
                s = SpGrp( n+1, sn+1 )
                info( s )

