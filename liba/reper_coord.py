from mat import *

def dec2frac( self, arg ):
    """ Return vector in fractional local coordinate system.
        arg:  list of vectors or vec desribed in decart system.
    """
    els = list( self.v1 ) + list( self.v2 ) + list( self.v3 )
    m = Mat( *els ).t().inv()

    ## TODO: may be better detection of list, tuples, sets ... (iterables)
    if not isinstance( arg, Vec ):
        try:
            return map( lambda v: m * v, arg )
        except:
            return m * arg
    else:
        return m * arg


def frac2dec( self, arg ):
    """ Convert from fractional to decart coordinate system.
        arg:  list of vectors or vec desribed in decart system.
    """
    els = list( self.v1 ) + list( self.v2 ) + list( self.v3 )
    m = Mat( *els ).t()

    if not isinstance( arg, Vec ):
        try:
            return map( lambda v: m * v, arg )
        except:
            return m * arg
    else:
        return m * arg



import reper
reper.Reper.dec2frac = dec2frac
reper.Reper.frac2dec = frac2dec
