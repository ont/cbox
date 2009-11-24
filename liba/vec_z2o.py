import math
from vec import Vec

def z2o( self ):
    """ Coorect all vector coordinates to be in [0,1) interval
    """
    xyz = map( lambda x: x - math.floor( x ), self )
    return Vec( *xyz )


import vec
vec.Vec.z2o = z2o
