import zell
from zell import Zell

def norm( self ):
    """Return symbol in normal form
       g,h,k,l,m,n <= 0
    """
    p = ( 3,4,5,0,1,2 )                              ## pairs
    s = ( (4,2), (3,2), (3,1), (4,5), (5,3), (4,3) ) ## swaps

    l = list( self )
    while filter( lambda e: e > 0.00001, l ):
        for i in xrange( 6 ):
            if l[ i ] > 0:
                ln = [ e + l[ i ] for e in l ]      ## all +g
                ln[ i ] = -l[ i ]                   ## g = -g
                ln[ p[ i ] ] = l[ p[ i ] ] - l[ i ] ## pair -g

                a,b = ln[ s[i][0] ], ln[ s[i][1] ]  ## swap
                ln[ s[i][0] ], ln[ s[i][1] ] = b,a

                l = ln

    return Zell( *l )




zell.Zell.norm = norm
