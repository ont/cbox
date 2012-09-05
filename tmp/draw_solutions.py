import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from draw_gl import drawgl

from vec   import *
from voron import *

import vec_gl
import voron_gl

vo = Voron( Vec( 1.0, 0.0, 0.0 ),
            Vec( 0.0, 1.0, 0.0 ),
            Vec( 0.0, 0.0, 1.0 ) )

drawgl( vo )
drawgl.start()
