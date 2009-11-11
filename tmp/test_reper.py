import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from vec   import *
from reper import *
import reper_min
r = Reper( Vec( 1, 0, 0 ),
           Vec( 8, 1, 0 ),
           Vec( 0, 0, 1 ) )

print r
print r.minimize()

