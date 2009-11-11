from mat  import Mat
from vec  import Vec

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


    def __len__( self ):
        return len( self.mydata['gens'] )


    def __getitem__( self, n ):
        e = self.mydata['gens'][ n ]
        m = self.genr[ e[0] - 1 ]
        t =  Vec( *e[1] )
        return ( m, t )


    def cvecs( self ):
        """ Return centering vectors for this space group.
        """
        typ = self.mydata['symb'][0]
        ##TODO: find vectors for B and test for A and C and R
        vs = { 'A':[ Vec( 0, 0.5, 0.5 ) ],
               'C':[ Vec( 0.5, 0.5, 0 ) ],
               'B':None,
               'F':[ Vec( 0, 0.5, 0.5 ),Vec( 0.5, 0, 0.5 ), Vec( 0.5, 0.5, 0 ) ],
               'I':[ Vec( 0.5, 0.5, 0.5 ) ],
               'P':[],
               'R':[ Vec( 2.0/3.0, 1.0/3.0, 1.0/3.0 ),
                     Vec( 1.0/3.0, 2.0/3.0, 2.0/3.0 ) ]
             }
        return vs[ typ ]


    def __mul__( self, v ):
        res = [ v ]
        cnt = ( 1,1,1,1,1,1,1,1,1,1,1,2,2,3,3 )  ## how many times to apply generator...
        for e in self.mydata['gens']:
            m = self.genr[ e[0] - 1 ]
            t = Vec( *e[1] )
            l = []
            for v in res:
                tv = v
                for i in xrange( cnt[ e[0] ] ):
                    tv = m * tv + t
                    l.append( tv )

            res.extend( l )

        l = []
        for v in res:
            for vc in self.cvecs():
                l.append( v + vc )
        res.extend( l )

        return list( set( res ) )


    def __repr__( self ):
        return "SpGrp( num = %s, snum = %s )" % ( self.num, self.snum )


import os, pickle
pdir = os.path.dirname( __file__ )

SpGrp.data = pickle.load( open(  os.path.join( pdir , 'spgrp.pkl' ), 'rb' ) )

SpGrp.genr = [
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
