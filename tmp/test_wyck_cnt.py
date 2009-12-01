import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from spgrp import *
import spgrp_wyck

ans =\
{  15 : [4,4,4,4],
   70 : [8,8,16,16],
  111 : [1,1,1,1,2,2],
  123 : [1,1,1,1,2,2],
  133 : [4,4,4,4,8],
  148 : [1,1,3,3],
  200 : [1,1,3,3],
  209 : [4,4,8,24],
  212 : [4,4],
  222 : [2,6,8,12],
  225 : [4,4,8,24],
  226 : [8,8,24,24],
  230 : [16,16,24,24] }

for n in (15,70,111,123,133,148,200,209,212,222,225,226):
    for ns in xrange( len( SpGrp.data[ n-1 ] ) ):
        s = SpGrp( n, ns+1 )
        lens = map( len, s.wyckiter() )
        print s, '--->', lens, ans[n] == lens

s = SpGrp( 166, 1 )
lens = map( len, s.wyckiter() )
print s,'--->', lens   #TODO: must be [3,3,9,9] because of centering
print s.mydata
#print s.gens2set( list( s ) )

s = SpGrp( 166, 2 )
lens = map( len, s.wyckiter() )
print s,'--->', lens
print s.mydata

