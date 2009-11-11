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
                ("O11"  , (1, 2, 1, 1, 3, 1)),
                ("O12"  , (1, 3, 2, 1, 3, 2)),
                ("O2"   , (1, 0, 2, 2, 3, 1)),
                ("O3"   , (1, 0, 2, 1, 0, 2)),
                ("O4"   , (0, 2, 0, 1, 3, 1)),
                ("O5"   , (0, 0, 0, 1, 2, 3)),
                ("+O3"  , (1, 0, 2, 2, 0, 1)),
                ("+O4"  , (0, 1, 0, 1, 2, 3)),
                ("+O5"  , (0, 0, 1, 0, 2, 3)),
                ("M11"  , (1, 3, 2, 1, 4, 2)),
                ("M12"  , (1, 3, 1, 2, 4, 2)),
                ("M21"  , (1, 2, 3, 4, 5, 1)),
                ("M22"  , (1, 0, 2, 1, 3, 2)),
                ("M3"   , (1, 0, 2, 1, 0, 3)),
                ("M4"   , (0, 1, 0, 2, 3, 4)),
                ("+M22" , (2, 0, 2, 1, 3, 1)),
                ("+M3"  , (2, 0, 1, 1, 0, 3)),
                ("T1"   , (1, 2, 3, 4, 5, 6)),
                ("T2"   , (1, 0, 2, 3, 4, 5)),
                ("T3"   , (1, 0, 2, 3, 0, 4))
            )

    def test( c, z ):
        g = {}
        for i in xrange( 6 ):
            n = c[ i ]
            if ( n == 0 and abs( z[ i ] ) > 0.001 ) or\
               ( n != 0 and abs( z[ i ] ) < 0.001 ):     ## zeroes only on zeores
                return False
            else:
                v = g.get( n, None )
                if v:                                    ## test with group
                    if abs( z[ i ] - v ) > 0.001:
                        return False
                else:
                    g[ n ] = z[ i ]                      ## new group

        return True


    z = self.norm()
    for c in cond:
        for p in xrange( 24 ):
            zr = z.rotate( p )

            if test( c[ 1 ], zr ):
                return Sort( c[ 0 ] )


import zell
zell.Zell.to_sort = to_sort

