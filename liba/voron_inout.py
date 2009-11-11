import math

from vec   import Vec
from reper import Reper

import vec_z2o
import reper_min
import reper_coord



def cut( self, pnts ):
    """ Cut 3d space assuming pnts are belong to crystal lattice.
        pnts: pnts in decart coordinate system
    """

    pin  = self.has( pnts )
    ptch = self.touch( pnts )
    pout = filter( lambda p: p not in pin, pnts )

    pout += ptch


    r = self.rep.minimize()
    pout = r.dec2frac( pout )
    pout = map( lambda v: v.z2o(), pout )

    p_ch = set()
    ds = [ (i,j,k) for i in xrange( -1, 1 )\
                   for j in xrange( -1, 1 )\
                   for k in xrange( -1, 1 ) ]
    vx = Vec( 1, 0, 0 )
    vy = Vec( 0, 1, 0 )
    vz = Vec( 0, 0, 1 )
    for p in pout:
        for dx, dy, dz in ds:
            v = r.frac2dec( self.pos + dx * vx + dy * vy + dz * vz + p )
            if self.has( v ):
                p_ch.add( v )

    return pin + list( p_ch )



def touch( self, arg ):
    """Test either point touch polyhedra or not.
       arg: point or points in decart coordinate system
    """
    ps = map( lambda p: ( p.norm( bvec = self.pos ),
                          p.center() + self.pos ),
              self.mesh.polys )

    def test( pnt ):
        for n,c in ps:
            if abs( n * ( pnt - c ) ) < 0.0001:
                return True
        return False

    try:
        pin = self.has( arg )
        return filter( test, pin )
    except:
        pin = self.has( [arg] )
        return filter( test, pin )



def has( self, arg ):
    """Test either point inside polyhedra or not.
       arg: point or points in decart coordinate system
    """
    ps = map( lambda p: ( p.norm( bvec = self.pos ),
                          p.center() + self.pos ),
              self.mesh.polys )

    def test( pnt ):
        for n,c in ps:
            if n * ( pnt - c ) > 0.0001:
                return False
        return True

    try:
        return filter( test, arg   )
    except:
        return filter( test, [arg] )



import voron
voron.Voron.cut = cut
voron.Voron.has = has
voron.Voron.touch = touch
