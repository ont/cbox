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

    def __repr__( self ):
        return 'reper( %s,%s,%s )' % ( self.v1, self.v2, self.v3 )

