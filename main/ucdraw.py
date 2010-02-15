#!/usr/bin/env python
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from draw_gl import drawgl
from strutils import *

from voron import *

import voron_gl
import ucell_gl

ls = list( stdlines() )

opts = sys.argv[ 1: ]
print opts

for i,u in enumerate( lines2cells( ls ) ):
    v = Voron( *u.rep )
    if i < len( opts ) :
        if opts[ i ] == '1':
            drawgl( u )
    else:
        drawgl( u )

    drawgl( v )

drawgl.start()
