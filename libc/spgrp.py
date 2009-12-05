from mat  import Mat
from vec  import Vec

import vec_z2o

class SpGrp( object ):
    data = None   ## here all info about all space groups
                  ## data[ num ][ snum ] = { inv  =  has inversion element
                  ##                         ngp  =  number of general positions
                  ##                         symb =  Her. Mau. symbol
                  ##                         rcnd =  reflection conditions
                  ##                         wyck =  wyckoff positions
                  ##                         gens =  generators ( type, (x,y,z) )

    genr = None   ## all matrices for generators

    def __init__( self, num, snum ):
        self.num  = num
        self.snum = snum
        self.mydata = self.data[ self.num-1 ][ self.snum-1 ]

        self.gens = self.mydata['gens']
        self.gens.append( ( 0, (0.0, 0.0, 0.0) ) )
        self.gens.reverse()
        if self.mydata['inv']:
            self.gens.append( ( 1, (0.0, 0.0, 0.0) ) )


    def __len__( self ):
        return len( self.gens )


    def __getitem__( self, n ):

        e = self.gens[ n ]
        m = self.genr[ e[0] ]
        t =  Vec( *e[1] )
        return ( m, t )


    @classmethod
    def subs( klas, num ):
        return xrange( 1, len( klas.data[ num-1 ] ) + 1 )


    def cvecs( self ):
        """ Return centering vectors for this space group.
        """
        typ = self.mydata['symb'][0]
        ##TODO: find vectors for B and test for A and C and R
        ##TODO: http://img.chem.ucl.ac.uk/sgp/large/146az1.htm
        vs = { 'A':[ Vec( 0, 0.5, 0.5 ) ],
               'C':[ Vec( 0.5, 0.5, 0 ) ],
               'B':[], ##TODO: <<< error
               'F':[ Vec( 0, 0.5, 0.5 ),Vec( 0.5, 0, 0.5 ), Vec( 0.5, 0.5, 0 ) ],
               'I':[ Vec( 0.5, 0.5, 0.5 ) ],
               'P':[],
               'R':[]  ##TODO: <<< error  (some coordinate orientation has +(2/3,1/3,1/3),(1/3,2/3,2/3)
             }
        return vs[ typ ]


    def __mul__( self, v ):
        """Vector v must be in fractional coordinate system.
        """
        res = set([ v ])
        for e in self.gens:
            m = self.genr[ e[0] ]
            t = Vec( *e[1] )
            toadd = set()
            for v in res:  ## apply generator to each vec in result set
                l = []     ## l = [ e * v, e^2 * v, e^3 * v, ... ]
                tv = v.z2o()
                while tv not in l:
                    l.append( tv )
                    tv = m * tv + t
                    tv = tv.z2o()   ## cut to unit volume

                toadd.update( l )


            #    for i in xrange( cnt[ e[0] - 1 ] ):
            #        tv = m * tv + t
            #        l.append( tv )

            res.update( toadd )

        l = []
        for v in res:
            for vc in self.cvecs():
                l.append( (v + vc).z2o() )
        res.update( l )

        return list( res )


    def __repr__( self ):
        return "SpGrp( num = %s, snum = %s )" % ( self.num, self.snum )


import os, pickle
pdir = os.path.dirname( __file__ )

SpGrp.data = pickle.load( open(  os.path.join( pdir , 'spgrp.pkl' ), 'rb' ) )

SpGrp.genr = [
        Mat(  1,  0,  0,
              0,  1,  0,    ##  1
              0,  0,  1 ),

        Mat( -1,  0,  0,
              0, -1,  0,    ## -1
              0,  0, -1 ),

        Mat(  1,  0,  0,
              0, -1,  0,    ## 2_x
              0,  0, -1 ),

        Mat( -1,  0,  0,
              0,  1,  0,    ## 2_y
              0,  0, -1 ),

        Mat( -1,  0,  0,
              0, -1,  0,    ## 2_z
              0,  0,  1 ),

        Mat(  0,  1,  0,
              1,  0,  0,    ## 2_110
              0,  0, -1 ),

        Mat(  0, -1,  0,
             -1,  0,  0,    ## 2_1-10
              0,  0, -1 ),

        Mat( -1,  0,  0,
              0,  1,  0,    ## m_x
              0,  0,  1 ),

        Mat(  1,  0,  0,
              0, -1,  0,    ## m_y
              0,  0,  1 ),

        Mat(  1,  0,  0,
              0,  1,  0,    ## m_z
              0,  0, -1 ),

        Mat(  0,  1,  0,
              1,  0,  0,    ## m_xxz
              0,  0,  1 ),

        Mat(  0, -1,  0,
             -1,  0,  0,    ## m_(x-xz)
              0,  0,  1 ),

        Mat(  0, -1,  0,
              1, -1,  0,    ## 3
              0,  0,  1 ),

        Mat(  0,  0,  1,
              1,  0,  0,    ## 3_111
              0,  1,  0 ),

        Mat(  0, -1,  0,
              1,  0,  0,    ## 4
              0,  0,  1 ),

        Mat(  0,  1,  0,
             -1,  0,  0,    ## -4
              0,  0, -1 )
        ]


if __name__ == "__main__":
    print SpGrp.data[ 224 ][ 0 ]
    s = SpGrp( 225, 1 )
    print len( s * Vec( 0.25, 0.25, 0.25 ) )

    l = set()
    for g in SpGrp.data:
        for sg in g:
            l.add( sg['symb'][0] )

    print l
