#!/usr/bin/env python2
import sys
import argparse
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from ucell import *
#from spgrp import *

p = argparse.ArgumentParser( description = 'Unit cell manipulation toolbox' )
g = p.add_argument_group( 'input data' )
g.add_argument( '-a', '--atoms', type = argparse.FileType('r'), help = 'file with atoms in each line in format "name  x  y  z"' )
g.add_argument( 'data', nargs = '+', type=float, help = 'unit cell definition in form "a b c alpha beta gamma" or "x_i y_i z_i" for i=1..3' )
g = p.add_argument_group( 'actions' )
g.add_argument( '-m', '--min' ,  action = 'store_true', help = 'minimize unit cell to primitive cell (with smallest possible basis)' )
g = p.add_argument_group( 'info' )
g.add_argument( '-i', '--info',  action = 'store_true', help = 'get full info about unit cell' )
g.add_argument( '-s', '--sort',  action = 'store_true', help = 'get info about sort of unit cell reper' )
g.add_argument( '-z', '--zell',  action = 'store_true', help = 'get zelling symbol for reper of unit cell' )
g.add_argument( '-v', '--voron', action = 'store_true', help = 'build Voronoi cell' )

args = p.parse_args()
if len( args.data ) not in (6,9):
    print 'wrong count of data\'s!'
    exit( 1 )

u = UCell( *args.data, indeg = True )

def sort():
    import reper2zell
    import zell2sort
    print 'sort:', u.rep.to_zell().to_sort()


def zell():
    import reper2zell
    import zell_norm
    print 'zell:', u.rep.to_zell().norm()

def voron():
    from draw_gl import drawgl
    from voron import Voron
    import voron_gl
    v = Voron( *u.rep )
    drawgl( v )
    drawgl.start()

if args.atoms:
    for l in args.atoms:
        arr = l.split()
        name, [x,y,z] = arr[ 0 ], map( float, arr[ 1: ] )[ :3 ]
        u[ name ].append( Vec( x,y,z ) )

if args.min:
    import ucell_min
    u = u.to_min()

if args.info:
    print u
    sort()
    for k,vs in u.atoms.iteritems():
        for v in vs:
            print k, v.x, v.y, v.z

if args.sort:
    sort()

if args.zell:
    zell()

if args.voron:
    voron()
