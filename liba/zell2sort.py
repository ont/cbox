import zell
from sort import Sort

import zell_norm    ## aspect
import zell_rotate  ## aspect

def to_sort( self ):
    cond = (
                ("K1"   , (1, 1, 1, 1, 1, 1)),
                ("K3"   , (1, 0, 1, 1, 0, 1)),
                ("K5"   , (0, 0, 0, 1, 1, 1)),

                ("H4"   , (0, 1, 0, 1, 2, 1)),
                ("Q1"   , (1, 2, 1, 1, 2, 1)),
                ("Q2"   , (1, 0, 1, 1, 2, 1)),
                ("Q5"   , (0, 0, 0, 1, 2, 1)),
                ("R1"   , (1, 1, 1, 2, 2, 2)),
                ("R3"   , (1, 0, 1, 1, 0, 2)),
                ("O3"   , (1, 0, 2, 1, 0, 2)),

                ("O4"   , (0, 2, 0, 1, 3, 1)),
                ("O11"  , (1, 2, 1, 1, 3, 1)),
                ("O12"  , (1, 3, 2, 1, 3, 2)),
                ("O2"   , (1, 0, 2, 2, 3, 1)),
                ("O5"   , (0, 0, 0, 1, 2, 3)),
                ("M22"  , (1, 0, 2, 1, 3, 2)),
                ("M3"   , (1, 0, 2, 1, 0, 3)),

                ("M11"  , (1, 3, 2, 1, 4, 2)),
                ("M12"  , (1, 3, 1, 2, 4, 2)),
                ("M21"  , (1, 0, 2, 3, 4, 1)),   # <<< ( 1, 2, 3, 4, 5, 1 )  error in Brave table !!!
                ("M4"   , (0, 1, 0, 2, 3, 4)),
                ("T3"   , (1, 0, 2, 3, 0, 4)),

                ("T2"   , (1, 0, 2, 3, 4, 5)),

                ("T1"   , (1, 2, 3, 4, 5, 6)),
           )

    def test( c, z ):
        g = {}
        for i in xrange( 6 ):
            n, v = c[ i ], abs( z[ i ] )
            g[ n ] = max( v, g.get( n, v ) )  ## store in group max possible abs value

        for i in xrange( 6 ):
            n = c[ i ]
            if ( n == 0 and abs( z[ i ] ) > 0.01 ) or\
               ( n != 0 and abs( z[ i ] ) < 0.01 ):     ## zeroes only on zeores
                return False
            elif n != 0 and ( g[ n ] - abs( z[ i ] ) ) / g[ n ] > 0.01:
                return False

        return True


    ## pairs to swap for each edge
    ps = { 0: [ (2,4), (1,5) ],
           1: [ (0,5), (2,3) ],
           2: [ (1,3), (0,4) ],
           3: [ (1,2), (4,5) ],
           4: [ (0,2), (3,5) ],
           5: [ (0,1), (3,4) ] }

    z = self.norm()

    ## generate all possible zellings for testing
    zs = set([])
    zs.update([ z.rotate( p ) for p in xrange( 24 ) ])  ## add all rotations
    for i, x in enumerate( z ):
        if x == 0:                                      ## hey! we can generate more symbols!
            p1, p2 = ps[ i ]                            ## take pairs for swapping
            for p in (p1, p2):                          ## for each pair...
                tmp = list( z )
                a,b = tmp[ p[0] ], tmp[ p[1] ]          ## current values
                tmp[ p[0] ], tmp[ p[1] ] = b,a          ## swap...
                zn = zell.Zell( *tmp )                  ## new zell symbol
                zs.update([ zn.rotate( p ) for p in xrange( 24 ) ])  ## add all rotations

    for c in cond:
        for z in zs:
            if test( c[ 1 ], z ):
                return Sort( c[ 0 ] )

    raise "Whaaaat!?  we can't find sort for %s ???" % self


zell.Zell.to_sort = to_sort
zell.Zell.cond =  {
            "K1"   : (1, 1, 1, 1, 1, 1),
            "K3"   : (1, 0, 1, 1, 0, 1),
            "K5"   : (0, 0, 0, 1, 1, 1),
            "H4"   : (0, 1, 0, 1, 2, 1),
            "Q1"   : (1, 2, 1, 1, 2, 1),
            "Q2"   : (1, 0, 1, 1, 2, 1),
            "Q5"   : (0, 0, 0, 1, 2, 1),
            "R1"   : (1, 1, 1, 2, 2, 2),
            "R3"   : (1, 0, 1, 1, 0, 2),
            "O11"  : (1, 2, 1, 1, 3, 1),
            "O12"  : (1, 3, 2, 1, 3, 2),
            "O2"   : (1, 0, 2, 2, 3, 1),
            "O3"   : (1, 0, 2, 1, 0, 2),
            "O4"   : (0, 2, 0, 1, 3, 1),
            "O5"   : (0, 0, 0, 1, 2, 3),
            "+O3"  : (1, 0, 2, 2, 0, 1),
            "+O4"  : (0, 1, 0, 1, 2, 3),
            "+O5"  : (0, 0, 1, 0, 2, 3),
            "M11"  : (1, 3, 2, 1, 4, 2),
            "M12"  : (1, 3, 1, 2, 4, 2),
            "M21"  : (1, 0, 2, 3, 4, 1),   # <<< ( 1, 2, 3, 4, 5, 1 )  error in Brave table !!!
            "M22"  : (1, 0, 2, 1, 3, 2),
            "M3"   : (1, 0, 2, 1, 0, 3),
            "M4"   : (0, 1, 0, 2, 3, 4),
            "+M22" : (2, 0, 2, 1, 3, 1),
            "+M3"  : (2, 0, 1, 1, 0, 3),
            "T1"   : (1, 2, 3, 4, 5, 6),
            "T2"   : (1, 0, 2, 3, 4, 5),
            "T3"   : (1, 0, 2, 3, 0, 4)
       }
