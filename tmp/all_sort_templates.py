####################################################
# This script found all possible equivalent 
# templates for each of 24 sorts.
####################################################

import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

## pairs to swap for each edge
ps = { 0: [ (2,4), (1,5) ],
       1: [ (0,5), (2,3) ],
       2: [ (1,3), (0,4) ],
       3: [ (1,2), (4,5) ],
       4: [ (0,2), (3,5) ],
       5: [ (0,1), (3,4) ] }

cond = ( 
    ("K1"   , (1, 1, 1, 1, 1, 1)),
    ("K3"   , (1, 0, 1, 1, 0, 1)),
    ("K5"   , (0, 0, 0, 1, 1, 1)),

    ("H4"   , (0, 1, 0, 1, 2, 1)),
    ("Q1"   , (1, 2, 1, 1, 2, 1)),
    ("Q2"   , (1, 0, 1, 1, 2, 1)),
    ("Q5"   , (0, 0, 0, 1, 2, 1)),
    ("R1"   , (1, 1, 1, 2, 2, 2)),
    ("R3"   , (1, 0, 1, 1, 0, 2)),
    ("O3"   , (1, 0, 2, 1, 0, 2)),

    ("O4"   , (0, 2, 0, 1, 3, 1)),
    ("O11"  , (1, 2, 1, 1, 3, 1)),
    ("O12"  , (1, 3, 2, 1, 3, 2)),
    ("O2"   , (1, 0, 2, 2, 3, 1)),
    ("O5"   , (0, 0, 0, 1, 2, 3)),
    ("M22"  , (1, 0, 2, 1, 3, 2)),
    ("M3"   , (1, 0, 2, 1, 0, 3)),

    ("M11"  , (1, 3, 2, 1, 4, 2)),
    ("M12"  , (1, 3, 1, 2, 4, 2)),
    ("M21"  , (1, 0, 2, 3, 4, 1)),   # <<< ( 1, 2, 3, 4, 5, 1 )  error in Brave table !!!
    ("M4"   , (0, 1, 0, 2, 3, 4)),
    ("T3"   , (1, 0, 2, 3, 0, 4)),

    ("T2"   , (1, 0, 2, 3, 4, 5)),

    ("T1"   , (1, 2, 3, 4, 5, 6))
)

from zell import *
import zell_rotate

for n, t in cond:
    s = set()
    s.add( t )  ## add current template to set
    for i, x in enumerate( t ):
        if not x:
            for p in ps[ i ]:
                tn = list( t )                 ## new template
                a,b = tn[ p[0] ], tn[ p[1] ]   ## take a,b
                tn[ p[0] ], tn[ p[1] ] = b,a   ## .. swap them in template
                
                z = Zell( *tn )
                if not s.intersection( set([ tuple( z.rotate( x ) ) for x in xrange( 24 ) ]) ):
                    s.add( tuple( tn ) )

    print ( n, list( s ) )


#z = Zell( 0, 0, -1, -1, 0, -1 )
#print '\n'.join([ str( z.rotate( i ) ) for i in xrange( 24 ) ])
