import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )


from vec   import *
from zell  import *
from voron import *

import zell2reper
import zell2sort

## drawing
from draw_gl import drawgl
from draw_ipe import drawipe
import voron_gl
import vec_gl


z = Zell( -1, 0, -3, -4, -5, -6 )
r = z.to_reper()
print z.to_sort()
#r = Zell( 0,0,0, -3, -3, -3 ).to_reper()
vo = Voron( *r )

#v1 = Vec( 1,0,0 )
#v2 = Vec( 0,3,0 )
#v3 = Vec( 0,0,9 )

def to_ipe( *args, **kargs ):
    #from math import *
    #al, th = drawgl.gl.alpha * pi / 180, drawgl.gl.theta * pi / 180
    #als = ( al, -al, al + pi / 2, al - pi / 2 )
    #ths = ( th, -th, th + pi / 2, th - pi / 2 )
    #for ai, al in enumerate( als ):
    #    for ti, th in enumerate( ths ):
    #        drawipe.setup( al, th, drawgl.gl.dist )
    #        drawipe.clear()
    #        drawipe.group()
    #        drawipe( v1, style = 'line' )
    #        drawipe( v2, style = 'line' )
    #        drawipe( v3, style = 'line' )
    #        drawipe.save( '/tmp/out_%s_%s.ipe' % ( ai, ti ) )
            
    #for i in xrange( 1,9 ):
    #    getattr( drawipe, 'setup_drawgl' + str( i ) )( drawgl )
    #    drawipe.clear()
    #    drawipe.group()
    #    drawipe( vo )
    #    drawipe.save( '/tmp/out%s.ipe' % i )

    drawipe.setup_drawgl( drawgl )
    drawipe.clear()
    drawipe.group()
    drawipe( vo )
    drawipe.save( '/tmp/out.ipe' )

#drawgl( v1, style = 'line' )
#drawgl( v2, style = 'line' )
#drawgl( v3, style = 'line' )
drawgl( vo )
drawgl.button( "to_ipe", to_ipe )
drawgl.start()
