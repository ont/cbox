from vec   import *
from spgrp import *

import spgrp_gens

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


def wyckiter( self ):
    """ Return iterator over all wyckoff positions.
    """

    def digitlist(value, numdigits=8, base=2):
        """ this is snipped from web ;)
        """
        val = value
        digits = [0 for i in range(numdigits)]
        for i in range(numdigits):
            val, digits[i] = divmod(val, base)
        return digits


    ns = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n')
    for w,n in zip( self.data[ self.num-1 ][ self.snum-1 ]['wyck'], ns ):
        if w[ 0 ] in deg0.keys():
            xyz = map( lambda s: eval( '1.0*' + s ), deg0[ w[ 0 ] ] )
            l = set( [ Vec( *xyz ) ] )

            dl = digitlist( w[ 1 ], len( self ) + 1 )      ## len( self ) == count of symm elems
            dl.reverse()
            #print '-------new-------'
            #print w[ 1 ], '--(binary)-->', dl
            #print w[ 1 ], '--(binary)-->', digitlist( w[ 1 ], 20 )


            ops = []
            for i,e in enumerate( self ):                  ## enumerate all symm elements
                if dl[ i ]:
                    ops.append( e )

            #print 'ops before = ', ops
            ops = self.gens2set( ops )
            #print 'ops after = ', ops

            ln = []
            for o in ops:
                for v in l:
                    ln.append( o[0] * v + o[1] )
            l.update( ln )


            ln = []
            for v in l:
                for vc in self.cvecs():
                    ln.append( v + vc )
            l.update( ln )

            yield list( l )
        else:
            #print "none :(", w
            pass


import spgrp
spgrp.SpGrp.wyckiter = wyckiter
