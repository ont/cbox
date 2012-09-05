import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )


from zell  import *
from voron import *
from reper import *

import zell2reper
import voron_gl

## drawing
from draw_gl import drawgl

p1,p2,p3 = -1,-1,-1

def redraw():
    global p1,p2,p3
    print "p1 = %s,  p2 = %s,  p3 = %s" % (p1,p2,p3)
    z = Zell( p1, 0, p2, p2, p3, p1 )
    vo = Voron( *z.to_reper() )
    drawgl.clear()
    drawgl( vo )

def inc_1( *args ):
    global p1
    p1 += 0.1
    redraw()

def dec_1( *args ):
    global p1
    p1 -= 0.1
    redraw()

def inc_2( *args ):
    global p2
    p2 += 0.1
    redraw()

def dec_2( *args ):
    global p2
    p2 -= 0.1
    redraw()

def inc_3( *args ):
    global p3
    p3 += 0.1
    redraw()

def dec_3( *args ):
    global p3
    p3 -= 0.1
    redraw()

drawgl.button( '+1', inc_1 )
drawgl.button( '-1', dec_1 )
drawgl.button( '+2', inc_2 )
drawgl.button( '-2', dec_2 )
drawgl.button( '+3', inc_3 )
drawgl.button( '-3', dec_3 )

drawgl.start()
