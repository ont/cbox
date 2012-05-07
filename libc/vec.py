from math import sqrt

class Vec( object ):
    def __init__( self, x, y, z ):
        self.set( x, y, z )

    def set( self, x, y, z ):
        self.x = x
        self.y = y
        self.z = z

    def to_int( self ):
        return Vec( int( self.x ), int( self.y ), int( self.z ) )

    def dist( self, other ):
        return ( self - other ).vlen()

    def norm( self ):
        return self * ( 1 / self.vlen() )

    def vlen( self ):
        return sqrt( self.x ** 2 + self.y ** 2 + self.z ** 2 )

    def vlen2( self ):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def __len__( self ):
        return 3

    def __add__( self, other ):
        return Vec( self.x + other.x, self.y + other.y, self.z + other.z )

    def __sub__( self, other ):
        return Vec( self.x - other.x, self.y - other.y, self.z - other.z )


    def vcross( self, v ):
        return Vec( v.z*self.y - v.y*self.z,
                    v.x*self.z - v.z*self.x,
                    v.y*self.x - v.x*self.y )

    def vdot( self, v ):
        return self.x*v.x + self.y*v.y + self.z*v.z

    def flat( self ):
        return ( self.x, self.y, self.z )

    def __mul__( self, o ):
        if type( o ) in ( int, float, long, complex ):
            return Vec( o * self.x, o * self.y, o * self.z )
        elif type( o ) is Vec:
            return self.vdot( o )


    def __rmul__( self, a ):
        return self * a

    def __getitem__( self, idx ):
        arr = ( self.x, self.y, self.z )
        return arr[ idx ]

    def __setitem__( self, idx, val ):
        if idx == 0:
            self.x = val
        elif idx == 1:
            self.y = val
        elif idx == 2:
            self.z = val


    def __hash__( self ):
        return 1 ## vec is not hashable
                 ## see stackoverflow site for this reason int( sum( self ) * 10 )


    def __eq__( self, other ):
        if abs( self.x - other.x ) < 0.001 and\
           abs( self.y - other.y ) < 0.001 and\
           abs( self.z - other.z ) < 0.001:
            return True
        else:
            return False

    def __repr__( self ):
        return "Vec( %s, %s, %s )" % ( 0 if abs( self.x ) < 0.0001 else self.x,
                                       0 if abs( self.y ) < 0.0001 else self.y,
                                       0 if abs( self.z ) < 0.0001 else self.z )


#v = Vec( 1, 1 )
#v2 = Vec( 3, 2 )
#print v2.dist( v )
