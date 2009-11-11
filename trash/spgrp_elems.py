import cPickle as pickle

from vec   import *
from mat   import *
from spgrp import SpGrp

from helpers import groupby



########## new abstractions ###########
class SGElem( object ):
    def __init__( self, m, v ):
        self.m = m
        self.v = v

    def mulI( self ):
        return SGElem( self.m.mulI(), self.v )

    def __mul__( self, v ):
        return self.m * v + self.v

    def __repr__( self ):
        m, v = self.m, self.v
        return "\nse( %4s %4s %4s | %4s\n    %4s %4s %4s | %4s\n    %4s %4s %4s | %4s )\n" % \
                ( m.m11, m.m12, m.m13, v[0], m.m21, m.m22, m.m23, v[1], m.m31, m.m32, m.m33, v[2] )



####### modify original classes #######
####### Mat
def mulI( self ):
    """Multiply matrix with inversion ( -1 0 0 | 0 -1 0 | 0 0 -1 )
    """
    return Mat( -self.m11,  self.m12,  self.m13,
                 self.m21, -self.m22,  self.m23,
                 self.m31,  self.m32, -self.m33 )

Mat.mulI = mulI



####### SpGrp
SpGrp.allelems = [ [] for i in xrange( 230 ) ]  ## 230 space groups
SpGrp.allhasI  = [ [] for i in xrange( 230 ) ]  ## has or not inversion element


def hasI( self ):
    """Return True if space group has invertion.
    """
    return SpGrp.allhasI[ self.num ][ self.snum ]


def elems( self ):
    """Return all symmetry elemns for space group
    """
    for e in SpGrp.allelems[ self.num ][ self.snum ]:
        yield e

        if self.hasI():
            yield e.mulI()


def __mul__( self, v ):
    """Multiply vector v with all symmetry elements
    """
    res = []
    for e in self.elems():
        res.append( e * v )

    return res

SpGrp.__mul__ = __mul__
SpGrp.hasI    = hasI
SpGrp.elems   = elems



######### prepare matrix tables #######
def prep_m():
    try:
        d = pickle.load( open( 'elems.pkl', 'rb' ) )
        SpGrp.allelems = d[ 0 ]
        SpGrp.allhasI  = d[ 1 ]

    except:                                                                 ## ... parse and save to file
        ls = open( 'elems.dat' ).readlines()
        ls = filter( lambda l: l, map( lambda l: l.strip(), ls ) )

        for sls in groupby( ls, 4 ):
            num, snum, inv, s, cnt = map( lambda s: int( s ), sls[ 0 ].split() )

            mats = [ Mat( 0,0,0,0,0,0,0,0,0 ) for i in xrange( cnt ) ]      ## create empty matrices
            vecs = [ Vec( 0,0,0 ) for i in xrange( cnt ) ]                  ## ..and empty vectors

            for i in xrange( 1, 4 ):
                prts = map( lambda s: float( s ), sls[ i ].split() )
                for j, els in enumerate( groupby( prts, 4 ) ):              ## group by (m11, m12, m13, v1) groups
                    mats[ j ][ i-1 ] = els[ :-1 ]                           ## set one row of matrix
                    vecs[ j ][ i-1 ] = els[  -1 ]                           ## set one coord of vec

            els = map( lambda e: SGElem( e[0], e[1] ), zip( mats, vecs ) )

            SpGrp.allelems[ num-1 ].append( els )                           ## SpGrp[ num ][ subnum ] = [ elem1, elem2, ... ]
            SpGrp.allhasI[ num-1 ].append( inv )


        f = open( 'elems.pkl', 'wb' )
        pickle.dump( ( SpGrp.allelems,
                       SpGrp.allhasI   ), f, -1 )
        f.close()



prep_m()  ## prepare matrices on module import


if __name__ == "__main__":
    s = SpGrp( 62 - 1, 3 - 1 )
    print len( SpGrp.allelems[ 1 ][ 1 ] )
    print list( s.elems() )
    print s * Vec( 0,0,0 )

