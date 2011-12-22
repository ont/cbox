import re
from cryst  import *
from spgrp  import *
from ucell  import *
from ucatom import *

## import aspects
import vec_z2o

class ICSD( object ):
    def __init__( self, fname ):
        self.fname = fname
        self.rnum  = re.compile( r'((\+|-){0,1}\d*\.{0,1}\d+(\(\d+\)){0,1})' )

    def str2num( self, s ):
        if '(' in s and '.' not in s:
            s = s.replace( '(', '.' )
        return float( s.replace( '(', '' ).replace( ')', '' ) )
        
    def __iter__( self ):
        """ iterate through each crystall in file
            returning Cryst instances
        """
        bad = False
        sp, uc, fats = None, None, False
        for l in open( self.fname ):
            if "*end for" in l and sp and uc:
                yield Cryst( sp, uc )
                sp, uc, fats = None, None, False

            if l[ 0:11 ] == "Space Group":
                sp = SpGrp.from_symb( ' '.join( l.split()[ 2: ] ) )
                if sp is None:
                    bad = True
                    print 'can\'t find', ' '.join( l.split()[ 2: ] )
                #assert sp is not None

            if l[ 0:9 ] == "SG Number":
                n = int( l.split()[ 2 ] )
                #sp = SpGrp( n, 1 )
                #if len( SpGrp.subs( n ) ) != 1:
                #    print 'WARN: more than one space group for number', n
                #    for sn in SpGrp.subs( n ):
                #        print sn + 1, SpGrp.data[ n - 1 ][ sn - 1 ]['symb']

                if bad:
                    print 'available groups for (%s):' % n
                    for sn in SpGrp.subs( n ):
                        print sn, SpGrp.data[ n - 1 ][ sn - 1 ]['symb']
                        print '----[gens]----'
                        print SpGrp( n, sn ).mydata['gens']
                        print '----[cvecs]----'
                        print SpGrp( n, sn ).cvecs()
                        print '----[ops]----'
                        for o in SpGrp( n, sn ):
                            print o
                    exit( 1 )

            if l[ 0:9 ] == "Unit Cell":
                abc = map( lambda s: self.str2num( s ), l.split()[ 2: ] )

            if fats:
                if l[ 0 ] == ' ':
                    name = l.split()[ 0 ]


                    #    0     |    1    |    2    |    3    |    4    |    5    |    6    |    7    |    8    |    9
                    #0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
                    # Re   6  +0    2 i   0.02585(3)  -.637110(14)-.164430(14)   1.         0               0

                    ## take first group in regexp ( t[ 0 ] ) of first 3 matches
                    x, y, z = [ self.str2num( t[ 0 ] ) for t in self.rnum.findall( l[ 21: ] )[ :3 ] ]

                    arr = uc[ name ]
                    arr.append( Vec( x, y, z ).z2o() )
                    uc[ name ] = arr

                else:
                    fats = False  ## end of atoms block

            if l[ 0:7 ] == "Atom  #" and not uc:   ## if atoms is not yet added
                fats = True
                uc = UCell( indeg = True, *abc )

                

                
        #sp = SpGrp( 1, 1 )
        #uc["A"] = ( Atom( 0.5, 0,0,0 ), Atom( 0.5, 0.5,0.5,0.5 ) )
        #for i in xrange( 3 ):
        #    yield Cryst( sp, uc )
