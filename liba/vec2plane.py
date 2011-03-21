from mat  import *
from vec  import *
from geom import *

def to_plane( self, r = None ):
    """ Return plane perpendicular to vector.
        r: point on plane
    """
    return Plane( n = self.norm(), r = r and r or self )


import vec
vec.Vec.to_plane = to_plane
