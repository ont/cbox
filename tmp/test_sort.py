import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from reper import *
from zell  import *
from vec   import *

import reper2zell
import zell2sort


r = Reper( Vec( 1.0, 0.0, 0.0 ),
           Vec( 0.0, 1.0, 0.0 ),
           Vec( 0.5, 0.5, 0.5 ) )

print dir( Zell )
print r.to_zell().to_sort()

print '-------------'
z = Zell( -1, 0, -2, -2, -3, -1 )
print z, z.to_sort()
z = Zell( -1, 0, -2, -2, 0, -1 )
print z, z.to_sort()
