
class Zell( object ):
    """ Class wich store six scalar products of vectors in reper.
        Other name of this structure is Delone Symbol.
    """
    def __init__( self, g,h,k,l,m,n ):
        self.g, self.h, self.k, self.l, self.m, self.n = g, h, k, l, m, n


    def __len__( self ):
        return 6


    def __getitem__( self, idx ):
        t = ( self.g, self.h, self.k, self.l, self.m, self.n )
        return t[ idx ]

    def __hash__( self ):
        return 1 ## zell as a vec is not hashable
                 ## see stackoverflow site for this reason int( sum( self ) * 10 )


    def __eq__( self, other ):
        tmp = map( lambda t: abs( t[ 0 ] - t[ 1 ] ) < 0.001, zip( self, other ) )  ## how different each pair ?
        return filter( lambda x: not x, tmp ) == []                                ## does here exists too different ?


    def __repr__( self ):
        return "zell( %s %s %s %s %s %s )" % ( self.g, self.h, self.k, self.l, self.m, self.n )

