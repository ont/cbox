import reper
from vec   import *
from math  import *
from reper import Reper

@classmethod
def from_abc( klass, a,b,c, alpha, beta, gamma ):
    """ Create 3 vectors from six parameters
    """
    sin_gamma = sin( gamma )
    cos_gamma = cos( gamma )
    tan_gamma = tan( gamma )
    cos_beta  = cos( beta  )
    cos_alpha = cos( alpha )
    v1 = Vec( a, 0, 0 )
    v2 = Vec( b * cos_gamma,
              b * sin_gamma,
              0 )
    v3 = Vec(                 c * cos_beta,
                           -( c * cos_beta / tan_gamma ) + c * cos_alpha / sin_gamma,
               sqrt( c**2 - ( c * cos_beta )**2 - ( -( c * cos_beta / tan_gamma ) + c * cos_alpha / sin_gamma )**2 ) )
    return Reper( v1, v2, v3 )


reper.Reper.from_abc = from_abc
