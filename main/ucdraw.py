#!/usr/bin/env python
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from draw_gl import drawgl
from strutils import *

from voron import *

import voron_gl
import ucell_gl

ls = list( stdlines() )
u = lines2cell( ls )

v = Voron( *u.rep )

drawgl( v )
drawgl( u )

drawgl.start()
