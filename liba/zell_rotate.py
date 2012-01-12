import zell

def rotate( self, newpos ):
    """ Return new Delone symbol in one of 24 possible position.
    """
    trans = ( (0,1,2,3,4,5), (0,2,1,3,5,4), (0,4,5,3,1,2),
              (0,5,4,3,2,1), (1,0,2,4,3,5), (1,2,0,4,5,3),
              (1,3,5,4,0,2), (1,5,3,4,2,0), (2,0,1,5,3,4),
              (2,1,0,5,4,3), (2,3,4,5,0,1), (2,4,3,5,1,0),
              (3,1,5,0,4,2), (3,2,4,0,5,1), (3,4,2,0,1,5),
              (3,5,1,0,2,4), (4,0,5,1,3,2), (4,2,3,1,5,0),
              (4,3,2,1,0,5), (4,5,0,1,2,3), (5,0,4,2,3,1),
              (5,1,3,2,4,0), (5,3,1,2,0,4), (5,4,0,2,1,3) )

    arr = ( self.g, self.h, self.k, self.l, self.m, self.n )

    res = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
    for i in xrange( 6 ):
        res[ i ] = arr[ trans[ newpos % 24 ][ i ] ]

    return zell.Zell( *res )



zell.Zell.rotate = rotate
