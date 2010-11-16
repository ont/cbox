from vec   import *
from spgrp import *

import spgrp_gens
import vec_z2o

deg0 ={
  1  :  ("0"   , "0"   , "0"  ),
  32 :  ("1/4" , "1/4" , "0"  ),
  63 :  ("1/2" , "3/4" , "0"  ),
  2  :  ("0"   , "0"   , "1/4"),
  33 :  ("1/4" , "1/4" , "1/4"),
  64 :  ("1/2" , "3/4" , "1/4"),
  3  :  ("0"   , "0"   , "1/2"),
  34 :  ("1/4" , "1/4" , "1/2"),
  65 :  ("1/2" , "3/4" , "1/2"),
  4  :  ("0"   , "0"   , "3/4"),
  35 :  ("1/4" , "1/4" , "3/4"),
  66 :  ("1/2" , "3/4" , "3/4"),
  5  :  ("0"   , "1/4" , "0"  ),
  36 :  ("1/4" , "1/2" , "0"  ),
  67 :  ("5/8" , "0"   , "1/4"),
  6  :  ("0"   , "1/4" , "1/8"),
  37 :  ("1/4" , "1/2" , "1/4"),
  68 :  ("5/8" , "1/8" , "1/8"),
  7  :  ("0"   , "1/4" , "1/4"),
  38 :  ("1/4" , "1/2" , "1/2"),
  69 :  ("5/8" , "3/8" , "5/8"),
  8  :  ("0"   , "1/4" , "3/8"),
  39 :  ("1/4" , "1/2" , "3/4"),
  70 :  ("5/8" , "5/8" , "3/8"),
  9  :  ("0"   , "1/4" , "1/2"),
  40 :  ("1/4" , "3/4" , "0"  ),
  71 :  ("5/8" , "5/8" , "5/8"),
  10 :  ("0"   , "1/4" , "5/8"),
  41 :  ("1/4" , "3/4" , "1/4"),
  72 :  ("2/3" , "1/3" , "0"  ),
  11 :  ("0"   , "1/4" , "3/4"),
  42 :  ("1/4" , "3/4" , "1/2"),
  73 :  ("2/3" , "1/3" , "1/4"),
  12 :  ("0"   , "1/2" , "0"  ),
  43 :  ("1/4" , "3/4" , "3/4"),
  74 :  ("2/3" , "1/3" , "1/2"),
  13 :  ("0"   , "1/2" , "1/4"),
  44 :  ("1/3" , "2/3" , "0"  ),
  75 :  ("3/4" , "0"   , "0"  ),
  14 :  ("0"   , "1/2" , "1/2"),
  45 :  ("1/3" , "2/3" , "1/4"),
  76 :  ("3/4" , "0"   , "1/4"),
  15 :  ("0"   , "1/2" , "3/4"),
  46 :  ("1/3" , "2/3" , "1/2"),
  77 :  ("3/4" , "0"   , "1/2"),
  16 :  ("0"   , "3/4" , "0"  ),
  47 :  ("1/3" , "2/3" , "3/4"),
  78 :  ("3/4" , "1/4" , "0"  ),
  17 :  ("0"   , "3/4" , "1/8"),
  48 :  ("3/8" , "0"   , "1/4"),
  79 :  ("3/4" , "1/4" , "1/4"),
  18 :  ("0"   , "3/4" , "1/4"),
  49 :  ("3/8" , "1/8" , "1/8"),
  80 :  ("3/4" , "1/4" , "1/2"),
  19 :  ("0"   , "3/4" , "1/2"),
  50 :  ("3/8" , "3/8" , "3/8"),
  81 :  ("3/4" , "1/4" , "3/4"),
  20 :  ("1/8" , "0"   , "1/4"),
  51 :  ("1/2" , "0"   , "0"  ),
  82 :  ("3/4" , "1/2" , "0"  ),
  21 :  ("1/8" , "1/8" , "1/8"),
  52 :  ("1/2" , "0"   , "1/4"),
  83 :  ("3/4" , "1/2" , "1/4"),
  22 :  ("1/8" , "1/8" , "3/8"),
  53 :  ("1/2" , "0"   , "1/2"),
  84 :  ("3/4" , "1/2" , "1/2"),
  23 :  ("1/8" , "1/8" , "5/8"),
  54 :  ("1/2" , "0"   , "3/4"),
  85 :  ("3/4" , "1/2" , "3/4"),
  24 :  ("1/8" , "1/8" , "7/8"),
  55 :  ("1/2" , "1/4" , "0"  ),
  86 :  ("3/4" , "3/4" , "1/4"),
  25 :  ("1/8" , "3/8" , "1/8"),
  56 :  ("1/2" , "1/4" , "1/4"),
  87 :  ("3/4" , "3/4" , "1/2"),
  26 :  ("1/8" , "5/8" , "1/8"),
  57 :  ("1/2" , "1/4" , "1/2"),
  88 :  ("3/4" , "3/4" , "3/4"),
  27 :  ("1/8" , "7/8" , "1/8"),
  58 :  ("1/2" , "1/4" , "3/4"),
  89 :  ("7/8" , "0"   , "1/4"),
  28 :  ("1/4" , "0"   , "0"  ),
  59 :  ("1/2" , "1/2" , "0"  ),
  90 :  ("7/8" , "1/8" , "1/8"),
  29 :  ("1/4" , "0"   , "1/4"),
  60 :  ("1/2" , "1/2" , "1/4"),
  91 :  ("7/8" , "7/8" , "7/8"),
  30 :  ("1/4" , "0"   , "1/2"),
  61 :  ("1/2" , "1/2" , "1/2"),
  31 :  ("1/4" , "0"   , "3/4"),
  62 :  ("1/2" , "1/2" , "3/4") }


def digitlist(value, numdigits=8, base=2):
    """ this is snipped from web ;)
    """
    val = value
    digits = [0 for i in range(numdigits)]
    for i in range(numdigits):
        val, digits[i] = divmod(val, base)
    return digits


def wyckstab( self ):
    """ Return wyckoff position full
        subgroup of stabilizers.
    """
    for w in self.mydata['wyck']:
        dl = digitlist( w[ 1 ], len( self ) + 1 )      ## len( self ) == count of symm elems
        ops = []
        for i,e in enumerate( self ):  ## enumerate all symm elements
            if not dl[ i ]:
                ops.append( e )

        ## TODO: error for I * (0.5, 0.0, 0.0) ---> (-0.5, 0.0, 0.0) ---> (0.5,0.0,0.0)
        if w[ 0 ] in deg0.keys():
            xyz = map( lambda s: eval( '1.0*' + s ), deg0[ w[ 0 ] ] )
            wv = Vec( *xyz )  ## wyckoff vec
            if self.mydata['inv'] and ( self[ -1 ][ 0 ] * wv ).z2o() == wv:  ## append inversion to operations
                ops.append( self[ -1 ] )

        ops = self.gens2set( ops )


        ## test operations by hands
        ops_h = []
        if w[ 0 ] in deg0.keys():
            xyz = map( lambda s: eval( '1.0*' + s ), deg0[ w[ 0 ] ] )
            wv = Vec( *xyz )  ## wyckoff vec
            for e in self.full():
                if ( e[ 0 ] * wv + e[ 1 ] ).z2o() == wv:
                    ops_h.append( e )
            ops_h = self.gens2set( ops_h )

        yield ( ops, ops_h )



def wyckorb( self ):
    """ Return subgroup wich will orbit
        wyckoff position in unit cell.
    """
    for w in self.mydata['wyck']:
        dl = digitlist( w[ 1 ], len( self ) + 1 ) ## len( self ) == count of symm elems
        ops = []
        for i,e in enumerate( self ):  ## enumerate all symm elements
            if dl[ i ]:
                ops.append( e )

        ## TODO: error for I * (0.5, 0.0, 0.0) ---> (-0.5, 0.0, 0.0) ---> (0.5,0.0,0.0)
        if self.mydata['inv'] and w[ 0 ] != 1:  ## append inversion to operations
            ops.append( self[ -1 ] )

        ops = self.gens2set( ops )
        yield ops



def wyckpos( self ):
    """ Return iterator over all wyckoff positions.
    """
    #print 'self', '------------>', list( self )
    ns = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n')
    for w, ops in zip( self.mydata['wyck'], self.wyckorb() ):
        if w[ 0 ] in deg0.keys():
            xyz = map( lambda s: eval( '1.0*' + s ), deg0[ w[ 0 ] ] )
            wv = Vec( *xyz )  ## wyckoff vec

            #dl.reverse()
            #print '-------new-------'
            #print 'w =', w
            #print w[ 1 ], '--(binary)-->', dl
            #print w[ 1 ], '--(binary)-->', digitlist( w[ 1 ], 20 )
            #print 'wv =', wv
            #print 'self', '------------>', list( self )



            res = set()
            res.add( wv )

            #print '--(3)-- apply ops'
            for o in ops:
                res.add( ( o[0] * wv + o[1] ).z2o() )

            #print res
            #print 'before cvecs --->', len( res )

            #print '--(4)-- centering...'
            l = []
            for v in res:
                for vc in self.cvecs():
                    l.append( (v + vc).z2o() )
            res.update( l )

            #print 'cvecs ---------->', self.cvecs()
            #print 'after  cvecs --->', len( res )

            yield list( res )
        else:
            yield []


import spgrp
spgrp.SpGrp.wyckpos = wyckpos
spgrp.SpGrp.wyckorb = wyckorb
spgrp.SpGrp.wyckstab = wyckstab
