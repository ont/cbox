from math   import sqrt
from vec    import Vec
from reper  import Reper

def to_reper( self ):
    """ Convert back to reper
    """
    g, h, k, l, m, n = self.g, self.h, self.k, self.l, self.m, self.n
    a = sqrt( - l - h - k )
    b = sqrt( - m - g - k )
    c = sqrt( - n - g - h )
    cos_al = g / ( b * c )
    cos_bt = h / ( c * a )
    cos_gm = k / ( a * b )
    sin_al = sqrt( 1 - cos_al ** 2 )
    sin_bt = sqrt( 1 - cos_bt ** 2 )
    sin_gm = sqrt( 1 - cos_gm ** 2 )

    v1 = Vec( a, 0, 0 )
    v2 = Vec( b * cos_gm, b * sin_gm, 0 )

    x = c * cos_bt
    y = ( b * c * cos_al - v2.x * x )/ v2.y
    z = sqrt( c**2 - x**2 - y**2 )
    v3 = Vec( x, y, z )

    return Reper( v1, v2, v3 )



import zell
zell.Zell.to_reper = to_reper
