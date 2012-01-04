#!/usr/bin/env python2
import sys
import argparse
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from spgrp import *
import spgrp_wyck

p = argparse.ArgumentParser( description = 'Spage group information retriever' )
p.add_argument( '-i', '--info', action = 'store_true', help = 'print info about space group' )
p.add_argument( '-g', '--gens', action = 'store_true', help = 'print space group generators' )
p.add_argument( '-o', '--ops' , action = 'store_true', help = 'print all space group operations' )
p.add_argument( '-w', '--wyck', action = 'store_true', help = 'show full set of all groups of wyckoff positions' )
p.add_argument( '--sym', metavar = 'NAME', help = 'view info by space group name (for example  "F m -3 m")' )
p.add_argument( 'num'  , type=int, nargs = '?', default = None, help = 'main number of space group' )
p.add_argument( 'snum' , type=int, nargs = '?', default = None, help = 'origin and orientation choice number' )

args = p.parse_args()
if not args.num and not args.snum and not args.sym:
    p.print_usage()
    exit( 1 )

def ops( s ):
    print '--------------[ operations ]------------'
    import spgrp_gens
    for i, (m,v) in enumerate( s.full() ):
        print '---- operation #%s:' % i,
        print m, v, '\n'


def gens( s ):
    print '--------------[ generators ]------------'
    print 'additional non-lattice translational vectors:', s.cvecs()
    print 'count of generators:', len( s )
    for i,o in enumerate( s ):
        print '---- generator #%s:' % i,
        print o[ 0 ], o[ 1 ], '\n'


def wyck( s ):
    print '--------------[ wyck pos   ]------------'
    for ws in s.wyckpos():
        print ws

def info( s ):
    print s
    gens( s )
    wyck( s )
    print '--------------[ metadata   ]------------'
    print s.mydata

if args.snum:
    s = SpGrp( args.num, args.snum )

elif args.num:
    print 'orientations for spgrp %s:' % args.num
    for sn,g in enumerate( SpGrp.data[ args.num-1 ] ):
        print '#%s -- %s' % ( sn + 1, g['symb'] )
    exit( 1 )

elif args.sym:
    for n,gs in enumerate( SpGrp.data ):
        for sn,g in enumerate( gs ):
            if g['symb'] == args.sym:
                s = SpGrp( n+1, sn+1 )

if args.info:
    info( s )

if args.wyck:
    wyck( s )

if args.gens:
    gens( s )

if args.ops:
    ops( s )
