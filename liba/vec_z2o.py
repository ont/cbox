import math
from vec import Vec

def z2o( self ):
    """ Coorect all vector coordinates to be in [0,1) interval
    """
    def f( x ):
        x = x - math.floor( x )
        if x > 0.999:
            x = 0
        return x

    xyz = map( f, self )
    return Vec( *xyz )


import vec
vec.Vec.z2o = z2o
