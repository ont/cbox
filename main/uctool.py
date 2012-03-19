#!/usr/bin/env python2
import os, sys
import argparse
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from ucell import *
#from spgrp import *

p = argparse.ArgumentParser( description = 'Unit cell manipulation toolbox' )
g = p.add_argument_group( 'input data' )
g.add_argument( '-g', '--spgrp', help = 'space group in format "NUM,SUBNUM" (two numbers separated by ",")' )
g.add_argument( '-a', '--atoms', type = argparse.FileType('r'), help = 'file with atoms in each line in format "name  x  y  z"' )
g.add_argument( 'data', nargs = '+', type=float, help = 'unit cell definition in form "a b c alpha beta gamma" or "x_i y_i z_i" for i=1..3' )
g = p.add_argument_group( 'actions' )
g.add_argument( '-m', '--min' ,  action = 'store_true', help = 'minimize unit cell to primitive cell (with smallest possible basis)' )
g = p.add_argument_group( 'info' )
g.add_argument( '-i', '--info',  action = 'store_true', help = 'get full info about unit cell' )
g.add_argument( '-s', '--sort',  action = 'store_true', help = 'get info about sort of unit cell reper' )
g.add_argument( '-z', '--zell',  action = 'store_true', help = 'get zelling symbol for reper of unit cell' )
g = p.add_argument_group( 'drawing' )
g.add_argument( '-p', '--ipe',   action = 'store_true', help = 'add "save to ipe" button in 3D view' )
g = g.add_mutually_exclusive_group()
g.add_argument( '-v', '--voron', action = 'store_true', help = 'build & draw Voronoi cell' )
g.add_argument( '-d', '--draw',  action = 'store_true', help = 'draw usual unit cell' )

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


def voron( to_ipe = False ):
    from draw_gl import drawgl
    from voron import Voron
    import vec_gl
    import ucell_gl
    import voron_gl
    import voron_inout

    def draw_with( eng ):
        eng.clear()
        vo = Voron( *u.rep )
        eng( vo )
        u.to_decart()
        for n, vs in u*1:                 ## for each atoms in extended unitcell
            r, col = UCell.data[ n ]
            col = [ x/255.0 for x in col ]

            for v in vo.touch( vs ):
                eng( v, r = r, color = col, invis = False )
                eng( n, pos = v )

            for v in vo.has( vs ):        ## only draw atoms which are in Voron cell
                if not vo.touch( v ):
                    eng( v, r = r, color = col, invis = False )
                    eng( n, pos = v )


    def save2ipe( *args ):
        from draw_ipe import drawipe
        i = 0
        fname = '/tmp/out_%s.ipe'
        while os.path.exists( fname % i ):
            i += 1
        fname = fname % i
        print 'saving to %s...' % fname
        drawipe.setup_drawgl( drawgl )
        draw_with( drawipe )
        drawipe.save( fname )

    def minimize( *args ):
        global u
        u = u.to_min()
        draw_with( drawgl )

    draw_with( drawgl )

    if to_ipe:
        drawgl.button( 'save to ipe', save2ipe )

    if args.min:
        drawgl.button( 'minimize', minimize )

    drawgl.start()


def draw( to_ipe = False ):
    from draw_gl import drawgl
    import vec_gl
    import ucell_gl
    drawgl( u )
    drawgl.start()

if args.atoms:
    for l in args.atoms:
        arr = l.split()
        name, [x,y,z] = arr[ 0 ], map( float, arr[ 1: ] )[ :3 ]
        u[ name ].append( Vec( x,y,z ) )

if args.spgrp:
    s = SpGrp( *map( int, args.spgrp.split(',') ) )
    u = u * s

if args.min:
    import ucell_min
    if not args.voron:
        u = u.to_min()  ## do minimization immidiately

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
    voron( args.ipe )
elif args.draw:
    draw( args.ipe )
