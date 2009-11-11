from vec  import *
from math import sqrt


class Edg( object ):
    def __init__( self, p1, p2 ):
        self.p1 = p1
        self.p2 = p2

    def __hash__( self ):
        return hash( self.p1 ) + hash( self.p2 )

    def __eq__( self, other ):
        return  ( self.p1 == other.p1 and self.p2 == other.p2 ) or \
                ( self.p1 == other.p2 and self.p2 == other.p1 )

    def __ne__( self, other ):
        return not self.__eq__( other )

    def __repr__( self ):
        return "Edg( p1 = %s, p2 = %s )" % ( self.p1, self.p2 )


class Poly( object ):
    def __init__( self, pnts ):
        assert len( pnts ) > 2, "Too few points in list"
        self.pnts = pnts
        self.edgs = []
        sp = pnts[ 0 ]
        for ep in pnts[ 1: ]:
            self.edgs.append( Edg( sp, ep ) )
            sp = ep
        self.edgs.append( Edg( sp, pnts[ 0 ] ) )


    def norm( self, bvec = None ):
        """ Return normal of polygon.
            bvec: determine negate halfspace
            (back from poly plane).
        """
        p1, p2, p3 = self.pnts[ 0:3 ]
        v1 = p2 - p1
        v2 = p3 - p1
        n = v1.vcross( v2 ).norm()

        if bvec is not None:
            v = bvec - p1
            if n.vdot( v ) > 0.001:  ## in the same half space
                n *= -1

        return n


    def center( self ):
        """ Return vector to center of polygon.
        """
        v = reduce( lambda a,b: a + b, self.pnts )
        return 1.0 / len( self.pnts ) * v


    def __repr__( self ):
        res = "Poly(\n"
        for p in self.pnts:
            res += str( p ) + "\n"
        return res + ")"



class Mesh( object ):
    def __init__( self, polys ):
        self.polys = polys
        self.uedgs = set( ( e for po in polys for e in po.edgs ) )

    def __repr__( self ):
        res = "Mesh(\n"
        for p in self.polys:
            res += str( p ) + "\n"
        return res + ")"


if __name__ == "__main__":
    e1 = Edg( Vec( 0,0,0 ), Vec( 0,0,1 ) )
    e2 = Edg( Vec( 0,0,0 ), Vec( 0,0,1.001 ) )
    s = set( [ e1, e2 ] )
    print s
    print e1 in [ e2 ]

    p = Poly( [ Vec( 0,0,0 ), Vec( 0,1,0 ), Vec( 1,0,0 ) ] )
    print p.norm( bvec = Vec( 0, 0, -1 ))
