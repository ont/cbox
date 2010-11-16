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

#for n in (15,70,111,123,133,148,200,209,212,222,225,226):
#    for ns in SpGrp.subs( n ):
#        s = SpGrp( n, ns )
#        if s.mydata['inv']:
#            print "YES"
#        lens = map( len, s.wyckpos() )
#        if ans[n] != lens:
#            print s, '--->', lens, ans[n] == lens


#print s.gens2set( list( s ) )


s = SpGrp( 67, 6 )
print s.mydata['symb']
print s.mydata['inv']
print 'wpos -->', map( len, s.wyckpos() )
print 'worb -->', map( len, s.wyckorb() )
print 'wstab -->', map( lambda s: len(s[0]), s.wyckstab() )
print 'wstab () -->', map( lambda s: ( len(s[0]), len(s[1]) ), s.wyckstab() )

for n in xrange( 1, 231 ):
    for ns in SpGrp.subs( n ):
        s = SpGrp( n, ns )
        #print "( %s, %s )" % ( n, ns )
        for t, p in zip( s.wyckstab(), s.wyckpos() ):
            ws, wsmy = t
            if wsmy and len( ws ) != len( wsmy ) and not s.cvecs() and s.mydata['symb'][0] != 'B':
                print "------------"
                print s
                print map( len, t )
                print 'pos = ', p
                print '--not my--'
                print t[ 0 ]
                print '--my--'
                print t[ 1 ]
