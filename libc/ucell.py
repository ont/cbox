import math
import reper_abc

from reper import Reper


class UCell( object ):
    def __init__( self, *args ):
        if len( args ) == 6:
            a,b,c, alpha, beta, gamma = args
            self.rep = Reper.from_abc( a,b,c, alpha, beta, gamma )
        else:
            self.rep = args[ 0 ]

        self.pnts = {}


    def add( self, name, pnts ):
        """ Add a group of named points (atoms)
            to unit cell.
            Points mus be in decart (not fractional) coordinate system.
        """
        self.pnts[ name ] = set( pnts )


    def __mul__( self, n ):
        """ Extend ucell in all directions by n
        """
        ns = [ (i,j,k) for i in xrange( -n, n+1 )\
                       for j in xrange( -n, n+1 )\
                       for k in xrange( -n, n+1 ) ]
        uc = UCell( self.rep )

        for k,vs in self.pnts.iteritems():
            toadd = set()
            for t in ns:
                vt = self.rep * t
                for v in vs:              ## for each vector with name "k"
                    toadd.add( v + vt )   ## translate v by reper in each directions
            uc.add( k, toadd )  ## add extended points with name "k"

        return uc


    def __add__( self, obj ):
        """ Translate ucell by obj
        """
        nc = UCell( self.rep )
        for k,vs in self.pnts.iteritems():
            vs = map( lambda v: v + obj, vs )  ## translate vectors
            nc.add( k, vs )
        return nc


    def __repr__( self ):
        rep = self.rep
        a,b,c = rep[0].vlen(), rep[1].vlen(), rep[2].vlen()
        gam = math.acos( rep[0].norm() * rep[1].norm() ) * 180 / math.pi
        bet = math.acos( rep[0].norm() * rep[2].norm() ) * 180 / math.pi
        alf = math.acos( rep[1].norm() * rep[2].norm() ) * 180 / math.pi

        return "UCell( a,b,c = (%s, %s, %s)  angles = (%s, %s, %s) )" % ( a,b,c, alf, bet, gam )

