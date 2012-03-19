
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

    def __setitem__( self, idx, val ):
        t = [ self.g, self.h, self.k, self.l, self.m, self.n ]
        t[ idx ] = val
        self.g, self.h, self.k, self.l, self.m, self.n = t

    def __hash__( self ):
        return 1 ## zell as a vec is not hashable
                 ## see stackoverflow site for this reason int( sum( self ) * 10 )


    def __eq__( self, other ):
        ## TODO: Zell( 0, 0, 1, 1, 0, 1 ) == Zell( 0, 0, 0, 1, 1, 1 )    (reper --> mininimize --> norm --> zell)
        for p in xrange( 24 ):
            z = self.rotate( p )
            tmp = map( lambda t: abs( t[ 0 ] - t[ 1 ] ) < 0.001, zip( z, other ) )  ## how different each pair ?
            if filter( lambda x: not x, tmp ) == []:                                ## does here exists too different ?
                return True
        return False

    def __ne__( self, other ):
        return not self.__eq__( other )

    def __mul__( self, other ):
        return Zell( *[ other * x for x in self ] )

    def __rmul__( self, other ):
        return self.__mul__( other )

    def __repr__( self ):
        return "Zell( %s, %s, %s, %s, %s, %s )" % tuple(( 0 if abs( x ) < 0.0001 else x for x in [ self.g, self.h, self.k, self.l, self.m, self.n ] ))

import zell_rotate   ## aspect in main file ?! o.O  (needed by __eq__)
