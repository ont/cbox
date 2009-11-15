from vec import *

class Mat( object ):
    def __init__( self, *args ):
        self.m11 = args[ 0 ]
        self.m12 = args[ 1 ]
        self.m13 = args[ 2 ]
        self.m21 = args[ 3 ]
        self.m22 = args[ 4 ]
        self.m23 = args[ 5 ]
        self.m31 = args[ 6 ]
        self.m32 = args[ 7 ]
        self.m33 = args[ 8 ]


    def t( self ):
        """ Return transposed matrix
        """
        m11, m12, m13, m21, m22, m23, m31, m32, m33 =  self.m11, self.m12, self.m13, self.m21, self.m22, self.m23, self.m31, self.m32, self.m33
        return Mat( m11, m21, m31,
                    m12, m22, m32,
                    m13, m23, m33 )


    def det( self ):
        m11, m12, m13, m21, m22, m23, m31, m32, m33 =  self.m11, self.m12, self.m13, self.m21, self.m22, self.m23, self.m31, self.m32, self.m33
        return m11*(m22*m33 - m23*m32) + m12*(m23*m31 - m21*m33) + m13*(m21*m32 - m22*m31)


    def inv( self ):
        m11, m12, m13, m21, m22, m23, m31, m32, m33 =  self.m11, self.m12, self.m13, self.m21, self.m22, self.m23, self.m31, self.m32, self.m33
        d = self.det()
        a11 = ( m22*m33 - m23*m32 ) / d
        a12 = ( m13*m32 - m12*m33 ) / d
        a13 = ( m12*m23 - m13*m22 ) / d

        a21 = ( m23*m31 - m21*m33 ) / d
        a22 = ( m11*m33 - m13*m31 ) / d
        a23 = ( m13*m21 - m11*m23 ) / d

        a31 = ( m21*m32 - m22*m31 ) / d
        a32 = ( m12*m31 - m11*m32 ) / d
        a33 = ( m11*m22 - m12*m21 ) / d

        return Mat( a11, a12, a13,
                    a21, a22, a23,
                    a31, a32, a33 )


    def __getitem__( self, row ):
        """ Return matrix elements in 2d array style.
        """
        if row == 0:
            return [ self.m11, self.m12, self.m13 ]
        elif row == 1:
            return [ self.m21, self.m22, self.m23 ]
        elif row == 2:
            return [ self.m31, self.m32, self.m33 ]


    def __mul__( self, other ):
        """ Multiply matrix with vector or matrix.
        """
        if type( other ) is Vec:
            v = other
            rv = Vec( self.m11 * v[0] + self.m12 * v[1] + self.m13 * v[2],
                      self.m21 * v[0] + self.m22 * v[1] + self.m23 * v[2],
                      self.m31 * v[0] + self.m32 * v[1] + self.m33 * v[2] )
            return rv

        elif type( other ) is Mat:
            arr = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]
            for i in xrange( 3 ):
                for j in xrange( 3 ):
                    arr[ i ][ j ] = sum( ( self[ i ][ k ] * other[ k ][ j ] for k in xrange( 3 ) ) )
            return Mat( *(arr[ 0 ] + arr[ 1 ] + arr[ 2 ]) )


    def __hash__( self ):
        return 1 ## can't be hashable A B C D E F ... X Y Z issue ---> sum( map( lambda x: int( x * 10 ), self[ 0 ] + self[ 1 ] + self[ 2 ] ) )


    def __eq__( self, other ):
        arr1 = self[ 0 ] + self[ 1 ] + self[ 2 ]
        arr2 = other[ 0 ] + other[ 1 ] + other[ 2 ]
        diff = map( lambda a,b: abs( a-b ), arr1, arr2 )
        for d in diff:
            if d > 0.001:
                return False
        return True


    def __repr__( self ):
        return "\nM(%3s %3s %3s\n  %3s %3s %3s\n  %3s %3s %3s )\n" % ( self.m11, self.m12, self.m13, self.m21, self.m22, self.m23, self.m31, self.m32, self.m33 )


if __name__ == '__main__':
    from math import *

    x = 0.7
    m = Mat(  cos( x ), sin( x ), 0.0,
             -sin( x ), cos( x ), 0.0,
              0.0,      0.0,      1.0 )

    print m * m.t()
    print m * m.inv()
