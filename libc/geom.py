
class Line( object ):
    pass


class Plane( object ):
    def __init__( self, n, r ):
        """ Create plane from:
            n: normal
            r: point on plane
        """
        self.n = n
        self.r = r
        self.do_norm()


    def do_norm( self ):
        """ Correct plane vectors.
            Return nothing.
        """
        n, r = self.n, self.r
        n = n.norm()
        r = n * ( r * n )
        self.n, self.r = n, r



    def __hash__( self ):
        return hash( self.n ) + hash( self.r )


    def __eq__( self, other ):
        return self.r == other.r and self.n == other.n


    def __repr__( self ):
        return "Plane( n = %s, r = %s )" % ( self.n, self.r )
