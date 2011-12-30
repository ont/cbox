####################################################
# This script found all unique rotations for each sort template
# templates for each of 24 sorts.
####################################################

import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from zell import *
import zell2sort
import zell_rotate

def test( zo, zn ):
    m = {}
    for xo, xn in zip( zo, zn ):
        if xo not in m:
            m[ xo ] = set([ xn ])  ## xo --> xn  (mapping)
        else:
            m[ xo ].add( xn )      ## add more pairs

    if 0 in m and 0 not in m[ 0 ]: ## zero maps to anything else ?
        return False

    return filter( lambda x: len( m[ x ] ) != 1, m ) == []  ## non one-to-one mappings exist ?
        

res = {}
for name, cs in Zell.cond.iteritems():
    zus = []   ## unique Zellings
    for c in cs:
        z = Zell( *c )
        for p in xrange( 24 ):
            zn = z.rotate( p )

            uniq = True
            for zu in zus:
                if test( zu, zn ):
                    uniq = False
                    break

            if uniq:
                zus.append( zn )
            
    res[ name ] = map( tuple, zus )
    #print name, c, len( zus ), map( tuple, zus )

print res
