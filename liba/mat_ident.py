import mat

def is_ident( self ):
    """ Test for ident matrix.
    """
    s = 0
    for i in xrange( 3 ):
        for j in xrange( 3 ):
            if i != j:
                s += abs( self[ i ][ j ] )

    if abs( self.m11 - 1.0 ) < 0.0001 and\
       abs( self.m22 - 1.0 ) < 0.0001 and\
       abs( self.m33 - 1.0 ) < 0.0001 and s < 0.0001:
       return True
    else:
       return False


mat.Mat.is_ident = is_ident
