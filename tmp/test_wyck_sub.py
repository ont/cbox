import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from math  import *

from vec   import *
from reper import *
from spgrp import *
from ucell import *

import ucell_min
import spgrp_wyck
import reper2zell
import zell2sort


from draw_gl import drawgl
import vec_gl
import ucell_gl


## cubic system
rep = Reper( Vec( 1.0, 0.0, 0.0 ),
             Vec( 0.0, 1.0, 0.0 ),
             Vec( 0.0, 0.0, 1.0 ) )

s = SpGrp( 230, 1 )
for n in xrange( 195, 231 ):
    for sn in SpGrp.subs( n ):
        s = SpGrp( n, sn )
        #ss = set()  ## sorts set
        ss = list()  ## sorts list
        for w in s.wyckpos():
            ## oh, yes, wyckpos must return some NON-POINT 
            ## wyckoff positions ( by now it returs empty list [] )
            if w:
                u = UCell( rep )
                u.add( 'A', w )
                u = u.to_min()
                #ss.add( '%s:%s->%s' % ( u.rep.to_zell().to_sort().name, len( w ), len( u.atoms[ 'A' ] ) ) )
                sort = u.rep.to_zell().to_sort().name
                ss.append( '%s:%s-%s' % ( sort, len( w ), len( u.atoms[ 'A' ] ) ) )

                if 'P' in s.mydata['symb'] and sort != 'K5':
                    print '#',
                if 'F' in s.mydata['symb'] and sort != 'K3':
                    print '#',
                if 'I' in s.mydata['symb'] and sort != 'K1':
                    print '#',
                #if len( w ) == 24:
                #    for v in w:
                #        drawgl( v, color = (0,255,0), r = 0.02 )
                #    drawgl( Vec( 1,0,0 ), color = (100,0,0), r = 0.025 )
                #    drawgl( Vec( 0,1,0 ), color = (100,0,0), r = 0.025 )
                #    drawgl( Vec( 0,0,1 ), color = (100,0,0), r = 0.025 )
                #    drawgl( u )
                #    print u.rep.to_zell().to_sort()
                #    drawgl.start()
                #    exit( 0 )


        print "(%s) %s [ %s ]" % ( s.num, s.mydata['symb'], " ".join( ss ) )


#for w in s.wyckiter():
#    u = UCell( 1,1,1, pi/2, pi/2, pi/2 )
#    u.add( 'A', w )
#    u = u.to_min()
#    if len( u.pnts['A'] ) == 1:
#        print '--', u
#        print '==', u.rep.to_zell().to_sort()
#        print '--', u.pnts
#        print '>>', w




#lens = map( len, s.wyckiter() )
#print s,'--->', lens
#print s.mydata

#print len( s.gens2set( list( s ) ) )

