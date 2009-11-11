from mat  import *
from vec  import *
from geom import *

def to_plane( self, r ):
    """ Return plane perpendicular to vector.
        r: point on plane
    """
    return Plane( n = self.norm(), r = r )


import vec
vec.Vec.to_plane = to_plane
