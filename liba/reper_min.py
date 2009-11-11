from reper import Reper

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




import reper
reper.Reper.minimize = minimize
