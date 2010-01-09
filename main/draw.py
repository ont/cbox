import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from draw_gl import drawgl
from strutils import *

from voron import *
from reper import *

import voron_gl
import ucell_gl

ls = list( stdlines() )
v1 = str2vec( ls[ 0 ] )
v2 = str2vec( ls[ 1 ] )
v3 = str2vec( ls[ 2 ] )

v = Voron( v1, v2, v3 )
u = lines2cell( Reper( v1, v2, v3 ), ls[ 3: ] )

drawgl( v )
drawgl( u )

drawgl.start()
