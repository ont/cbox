import math
import reper_abc

from vec   import Vec
from reper import Reper
from spgrp import SpGrp

## import aspect for reper
import reper_coord

class UCell( object ):
    def __init__( self, *args, **kargs ):
        if len( args ) == 6:
            a,b,c, alpha, beta, gamma = args
            if kargs.get( 'indeg', False ):
                self.rep = Reper.from_abc( a,b,c, alpha * math.pi / 180.0, beta * math.pi / 180.0, gamma * math.pi / 180.0 )
            else:
                self.rep = Reper.from_abc( a,b,c, alpha, beta, gamma )
        elif len( args ) == 9:
            self.rep = Reper( Vec( *args[0:3] ), Vec( *args[3:6] ), Vec( *args[6:9] ) )
        else:
            assert type( args[ 0 ] ) is Reper
            self.rep = args[ 0 ]

        self.atoms = {}
        self.decart = kargs.get( 'decart', False )  ## by default assume that all coordinates of atoms in fractional coordinates

    def add( self, name, atoms ):
        """ Add a group of named points (atoms)
            to unit cell.
            Points mus be in decart (not fractional) coordinate system.
        """
        self.atoms[ name ] = set( atoms )

    def __getitem__( self, n ):
        if n in self.atoms:
            return self.atoms[ n ]
        else:
            res = []
            self.atoms[ n ] = res
            return res

    def __setitem__( self, n, v ):
        self.atoms[ n ] = v

    def __iter__( self ):
        return self.atoms.iteritems()


    def to_fract( self ):
        """ convert all coordinates: decart --> fractional
        """
        if self.decart:
            for n, vs in self:
                self[ n ] = self.rep.dec2frac( vs )
            self.decart = False

    def to_decart( self ):
        """ convert all coordinates: fractional --> decart
        """
        if not self.decart:
            for n, vs in self:
                self[ n ] = self.rep.frac2dec( vs )
            self.decart = True

    def __mul__( self, o ):
        """ Multiply ucell with number and space group
        """
        decart = self.decart
        self.to_decart()
        if type( o ) is int:
            ns = [ (i,j,k) for i in xrange( -o, o+1 )\
                           for j in xrange( -o, o+1 )\
                           for k in xrange( -o, o+1 ) ]
            uc = UCell( self.rep, decart = True )

            for k,vs in self.atoms.iteritems():
                toadd = set()
                for t in ns:
                    vt = self.rep * t
                    for v in vs:              ## for each vector with name "k"
                        toadd.add( v + vt )   ## translate v by reper in each directions
                uc.add( k, toadd )            ## add extended points with name "k"

            if not decart:
                uc.to_fract()
            return uc

        elif type( o ) == SpGrp:
            uc = UCell( self.rep )
            for n, ats in self:
                tmp = set()
                for a in ats:
                    for v in o * a:                      ## multiply each atom position with space group
                        tmp.add( Vec( v.x, v.y, v.z ) )  ## ... and then add it
                uc[ n ] = list( tmp )                    ## transform to list and save
            return uc


    def __add__( self, obj ):
        """ Translate ucell by obj
        """
        if type( obj ) is Vec:
            nc = UCell( self.rep )
            for k,vs in self.atoms.iteritems():
                vs = map( lambda v: v + obj, vs )  ## translate vectors
                nc.add( k, vs )
            return nc
        elif type( obj ) is UCell:
            nc = UCell( self.rep )
            nc.atoms = dict( self.atoms ) ## make copy of self atoms

            for k,v in obj.atoms.iteritems():
                nc.atoms[ k ] = nc.atoms.get( k, [] ) + v ## add extended set of atoms

            return nc


    def __repr__( self ):
        rep = self.rep
        a,b,c = rep[0].vlen(), rep[1].vlen(), rep[2].vlen()
        gam = math.acos( rep[0].norm() * rep[1].norm() ) * 180 / math.pi
        bet = math.acos( rep[0].norm() * rep[2].norm() ) * 180 / math.pi
        alf = math.acos( rep[1].norm() * rep[2].norm() ) * 180 / math.pi

        return "UCell( a,b,c = (%s, %s, %s)  angles = (%s, %s, %s)  atoms = '%s' )" % ( a,b,c, alf, bet, gam, map( lambda t: "%s(%s)" % (t[0], len( t[1] )), self ) )

