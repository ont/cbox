#!/usr/bin/env python
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from strutils import *

import ucell_min

ls = list( stdlines() )
u = lines2cell( ls )
u = u.to_min()

print cell2lines( u )
