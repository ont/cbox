from zell import *

def to_zell( self ):
    """ Convert reper to zelling symbol
    """
    v1, v2, v3 = self.v1, self.v2, self.v3
    v4 = ( v1 + v2 + v3 ) * -1

    k = v1 * v2
    h = v1 * v3
    l = v1 * v4

    g = v2 * v3
    m = v2 * v4

    n = v3 * v4

    return Zell( g,h,k,l,m,n )



import reper
reper.Reper.to_zell = to_zell
