class UCell( object ):
    def __init__( self, a,b,c, alpha, beta, gamma ):
        self.a = a
        self.b = b
        self.c = c
        self.alpha = alpha
        self.beta  = beta
        self.gamma = gamma

    def __repr__( self ):
        return "UCell( a,b,c = (%s, %s, %s)  angles = (%s, %s, %s) )" % ( self.a, self.b, self.c, self.alpha, self.beta, self.gamma )

