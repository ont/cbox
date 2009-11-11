
def touch( self, arg ):
    """ arg: points or point
        return point wich lie on plane
    """
    def test( pnt ):
        return abs( self.n * ( self.r - pnt ) ) < 0.0001

    try:
        return filter( test, arg )
    except:
        return filter( test, ( arg ) )


import geom
geom.Plane.touch = touch
