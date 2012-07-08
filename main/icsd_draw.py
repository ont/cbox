#!/usr/bin/env python2
import sys
import argparse
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from icsd import *

from voron    import Voron
import reper2zell
import zell2sort

p = argparse.ArgumentParser( description = 'ICSD crystall drawer' )
p.add_argument( '-a', '--atoms', action = 'store_true', help = 'draw atoms in unit cell' )
p.add_argument( '-n', '--num', type = int, help = 'number of crystall from ICSD file to dump. You can skip this option to list crystalls' )
p.add_argument( '--testmin', action = 'store_true', help = 'try to refill origianl voronoi cell with minimized copies' )
p.add_argument( '--wycksub', action = 'store_true', help = 'also draw related sublattices Voronoi cells' )
p.add_argument( 'file', help = 'path to ICSD file to dump' )

args = p.parse_args()

if args.num is None:
    for i,c in enumerate( ICSD( args.file ) ):
        print '#%s' % i
        print c
    exit( 0 )
else:
    from draw_ipe import drawipe
    from draw_gl  import drawgl

    import vec_gl
    import ucell_gl
    import voron_gl
    import voron_inout

    import zell_norm
    import ucell_min
    import spgrp_wyck
    import zell2sort

    c = filter( lambda t: t[ 0 ] == args.num, enumerate( ICSD( args.file ) ) )[ 0 ][ 1 ]

    u_basis = UCell( c.ucell.rep )
    u_basis.atoms = dict( c.ucell.atoms )

    c.fill()
    print 'ICSD number: ', c.icsd
    u = c.ucell
    print 'sort of original cell: ', u.rep.to_zell().to_sort().name
    print 'zell of original cell: ', u.rep.to_zell().norm()


    def draw_with( eng ):
        eng.clear()
        vo = Voron( *u.rep )
        eng( vo )
        u.to_decart()

        if args.atoms:
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

        if args.wycksub:
            u.to_fract()
            Z = u.to_min().rep.minimize().to_zell().norm()
            for wname, ws in zip( 'abcdefghijklmnopqrstuvwxyz', c.spgrp.wyckpos() ):
                for n, vs in u_basis:
                    for v in vs:
                        if v in ws:
                            print '--(%s)-->' % wname, n, v, c.spgrp * v,
                            u4min = UCell( u_basis.rep )
                            u4min.add( 'A', ws )
                            u4min = u4min.to_min()

                            z = u4min.rep.minimize().to_zell().norm()
                            if Z != z:
                                print 'FOUND %s' % z.to_sort()
                                vo = Voron( *u4min.rep )
                                eng( vo )
                            else:
                                print 'not wyck sublattice'
                    


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


    def minimize( *xxx ):
        global args, u
        
        ## test mimimization for correction
        if args.testmin:
            vo = Voron( *u.rep )  ## original Voronoi cell
            u = u.to_min()
            u_exp = u * 1

            u_exp.to_decart()

            drawgl.clear()
            drawgl( vo )

            ## draw all atoms which are in "vo"
            for n, ats in u_exp:
                r, col = UCell.data[ n ]
                col = [ x/255.0 for x in col ]

                for v in vo.has( ats ):
                    drawgl( v, r = r, color = col, invis = False )

            ## now draw all cloned Voronoi cells
            #import reper2dots
            #for v in vo.cut( u.rep.to_dots( 1, 1, 1 ) ):
            #    drawgl( Voron( *u.rep, pos = v ) )
            drawgl( Voron( *u.rep ) )
                    

        ## usual minimization process
        else:
            u = u.to_min()
            print '------------'
            print 'sort of minimized cell: ', u.rep.to_zell().to_sort().name
            print 'zell of minimized cell: ', u.rep.to_zell().norm()
            draw_with( drawgl )
            


    draw_with( drawgl )

    drawgl.button( 'save to ipe', save2ipe )
    drawgl.button( 'minimize', minimize )

    drawgl.start()
