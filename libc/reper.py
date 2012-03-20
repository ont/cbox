class Reper( object ):
    def __init__( self, v1, v2, v3 ):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def __getitem__( self, n ):
        arr = ( self.v1, self.v2, self.v3 )
        return arr[ n ]

    def __len__( self ):
        return 3

    def __mul__( self, obj ):
        return self.v1 * obj[0] +\
               self.v2 * obj[1] +\
               self.v3 * obj[2]

    def __repr__( self ):
        return 'Reper( %s,%s,%s )' % ( self.v1, self.v2, self.v3 )

    def __eq__( self, other ):
        return self.v1 == other.v1 and self.v2 == other.v2 and self.v3 == other.v3

    def equal( self, other ):
        """ Test for equality using rotations and reindexing
        """
        return set( self ) == set( other )  ## have we the same set of vectors ?

    def flat( self ):
        """ Return all vectors coordinates as flat list.
            This is suitable for building matrix from reper.
        """
        return list( self.v1 ) + list( self.v2 ) + list( self.v3 )
