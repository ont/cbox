#from draw_gl import drawgl

from ucell import UCell
from reper import Reper

import reper_coord
import vec_z2o

def to_min( self ):
    decart = self.decart

    self.to_decart() ## transform coordinates to decart basis
    rep = self.rep   ## alias
    near = {}

    ext = self * 1   ## extend in all directions by 1

    mps = min( self.atoms.values(), key = lambda l: len( l ) )  ## "minimal points"
                                                                ## this is minimal group of points
    mps = list( mps )  ## convert set() to ordered list()

    #print "minimal points = ", mps

    eqv_dr = set()  ## all possible translations wich translate each point of
                    ## this ucell (self) to extended ucell (ext)

    #print '--[1]-- find eqv_dr'
    ## for each pair from mps...
    for i in xrange( len(mps) ):
        for j in xrange( i+1, len(mps) ):
            dr = mps[i] - mps[j]  ## vec to translate
            uct = self + dr       ## translated ucell

            eqv = True         ## translate equiv or not
            for k,vs in uct:   ## for each groups of atoms...  (k = group name, vs = list of positions)
                if not vs.issubset( ext.atoms[ k ] ):  ## some points not intersected with others
                    eqv = False
                    break
            if eqv:
                eqv_dr.add( dr )

    eqv_dr.update( list( rep ) )  ## add vectors from original reper

    #print "possible translations = ", eqv_dr

    ## sort vectors by its lengs
    eqv_dr = list( eqv_dr )
    eqv_dr.sort( key = lambda v: v.vlen() )

    #DEBUG DRAW
    #for v in eqv_dr:
    #    drawgl( v, style="line", color=(1,0,0) )

    #print '--[2]-- find v1,v2,v3'
    ## take first vector
    for v1 in eqv_dr:
        v2, v3 = None, None

        ## take second shorterst wich is not lie on one line with v1
        v1n = v1.norm()
        for v in eqv_dr:
            if not v1n == v.norm():
                #print v1n, v.norm()
                v2 = v
                break

        ## take third shortest wich is not coplanar with v1 and v2
        vc = v1.vcross( v2 )
        for v in eqv_dr:
            if abs( vc * v ) > 0.05:
                v3 = v
                break

        if v2 and v3: ## good solution founded
            nrep = Reper( v1,v2,v3 ) ## new reper
            break


    #DEBUG DRAW
    #for v in nrep:
    #    drawgl( v, style="line", color=(0,1,0) )
    #print '--[3]-- reduce ucell'

    uc   = UCell( nrep, decart = True )  ## all atoms in decart coordinate system

    ## reduce basis
    for k,vs in self.atoms.iteritems():
        vsn = nrep.dec2frac( vs )
        vsn = map( lambda v: v.z2o(), vsn )
        vsn = set( vsn )
        vsn = nrep.frac2dec( vsn )
        uc.add( k, vsn )


    if not decart:
        self.to_fract()  ## restore state of ucell
        uc.to_fract()    ## convert answer to the same coordinate system

    return uc
    #for v in ext.atoms['K']:
    #    drawgl( v, r = 0.06, color=(1,0,0) )



import ucell
ucell.UCell.to_min = to_min
