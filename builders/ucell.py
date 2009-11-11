from builder import *
from spgrp   import *

import spgrp_matrices  ## add aspect to space group



class BUCell( Builder ):
    __name__ = 'Unit cell builder'
    __input__ = { 'basis' : list,
                  'spgrp' : SpGrp }

    def __init__( self ):
