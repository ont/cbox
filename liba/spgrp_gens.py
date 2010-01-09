from vec import *
from mat import *

import vec_z2o


@classmethod
def gens2set( klas, gens ):
    """ Multiply all elements in gens and
        return unique symmetry elements.
    """
    gens.append( ( Mat( 1,0,0,
                        0,1,0,
                        0,0,1 ),
                   Vec( 0,0,0 ) ) )

    ns = set( gens )   ## new set
    os = set( )        ## old set
    while ns != os:
        os = set( ns ) ## copy constructor
        ns = []
        for e1 in os:
            for e2 in os:
                ns.append( ( e1[0]*e2[0],                   ## U1 * U2
                           ( e1[0]*e2[1] + e1[1]).z2o() ) ) ## (U1 * betta + alpha).z2o()
        ns = set( ns )

    return list( ns )


def full( self ):
    """ Return all symmetry elements for this
        space group which works in unit cell [0,1]
    """
    return spgrp.SpGrp.gens2set( list( self ) )  ## expand generators set


import spgrp
spgrp.SpGrp.gens2set = gens2set
spgrp.SpGrp.full = full
