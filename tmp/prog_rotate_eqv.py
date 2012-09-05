import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from zell  import *
import  zell_rotate

eqv = 'algsys(at([ans_G=ans_H, ans_H=ans_K, ans_K=ans_L, ans_L=ans_M, ans_M=ans_N, 4=5, 5=6 ],[1=0,2=0,3=0]), [4,5,6]);'
z  = Zell( 'g', 'h', 'k', 'l', 'm', 'n' )

for i in xrange( 24 ):
    zr = z.rotate( i )
    res = eqv[:]
    for j in xrange( 6 ):
        res = res.replace( str( j+1 ), zr[ j ] )
    print res
