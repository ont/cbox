from zell  import Zell
from reper import Reper

import reper2zell

def minimize( self ):
    """ Reduce reper to 3 minimal vector.
    """
    vs = [ self.v1, self.v2, self.v3 ]
    f = True
    while f:
        f = False
        vts = [ t for t in vs ]
        abc = ( (i,j,k) for i in xrange( -1, 2 )\
                        for j in xrange( -1, 2 )\
                        for k in xrange( -1, 2 ) )
        for a,b,c in abc:
            vnew = a * vs[ 0 ] + b * vs[ 1 ] + c * vs[ 2 ]
            for i, v in enumerate( vts ):
                if v.vlen2() > vnew.vlen2():
                    vo, vts[ i ] = vts[ i ], vnew
                    if abs( vts[0] * vts[1].vcross( vts[2] ) ) > 0.0001:
                        f = True
                    else:
                        vts[ i ] = vo
        #print vs, vts, f
        vs = vts

    return Reper( *vs )


def norm( self ):
    """ Reduce & make all zelling args negative.
    """
    vs = [ self.v1, self.v2, self.v3, ( self.v1 + self.v2 + self.v3 ) * -1 ]

    f = True
    while f:
        f = False
        for i, v1 in enumerate( vs ):
            for j, v2 in enumerate( vs ):
                if i != j and v1 * v2 > 0.0001:
                    for k in xrange( 4 ):
                        if k != i and k != j:
                            vs[ k ] += v1      ## add v1 to all, except v1 and v2
                    vs[ i ] *= -1              ## v1 --> -v1
                    v1 *= -1                   ## also correct cycle var
                    f = True

    return Reper( vs[0], vs[1], vs[2] )


import reper
reper.Reper.minimize = minimize
reper.Reper.norm     = norm
