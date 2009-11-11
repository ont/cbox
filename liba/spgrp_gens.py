from vec import *
from mat import *

import vec_z2o


def gens2set( self, gens ):
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
        ns = set( )
        for e1 in os:
            for e2 in os:
                ns.add( ( e1[0]*e2[0],                    ## U1 * U2
                          (e1[0]*e2[1] + e1[1]).z2o() ) ) ## (U1 * betta + alpha).z2o()
    return list( ns )


import spgrp
spgrp.SpGrp.gens2set = gens2set
