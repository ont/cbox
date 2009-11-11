
def to_dots( self, nx, ny, nz ):
    """Produce set of dots multiply each vector in
       interval (-nx,nx),...
    """
    ps = []
    for a,b,c in ( (i,j,k) for i in xrange( -nx,nx+1 )\
                           for j in xrange( -ny,ny+1 )\
                           for k in xrange( -nz,nz+1 ) ):
        ps.append( a*self.v1 + b*self.v2 + c*self.v3 )

    return ps

import reper
reper.Reper.to_dots = to_dots
