class Cryst( object ):
    """ Cryst is a container for UCell and SpGrp objects
    """
    def __init__( self, spgrp, ucell ):
        self.spgrp = spgrp
        self.ucell = ucell

    def fill( self ):
        """ populate unit cell with atoms from basis
        """
        self.ucell = self.ucell * self.spgrp

    def __repr__( self ):
        return "Cryst(\n\tspgrp = \"%s (%s)\"\n\tcvecs -> %s\n\tucell -> %s\n\tatoms -> %s\n)" % \
                ( self.spgrp.symb, 
                  self.spgrp.snum, 
                  self.spgrp.cvecs(),
                  self.ucell,
                  map( lambda t: "%s(%s)" % (t[0], len( t[1] )), self.ucell ) )
