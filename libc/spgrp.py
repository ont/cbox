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

    ## below are some aliases for ICSD crystallographic database
    syns = { (76 ,1): ['P 41'],
             (77 ,1): ['P 42'],
             (78 ,1): ['P 43'],
             (80 ,1): ['I 41'],
             (84 ,1): ['P 42/m'],
             (85 ,1): ['P 4/n S'],
             (85 ,2): ['P 4/n Z'],
             (86 ,1): ['P 42/n S'],
             (86 ,2): ['P 42/n Z'],
             (87 ,1): ['F 4/m'],   ## TODO: it is bug in ICSD! (must be "I 4/m", check bilbao crystallographic server)
             (88 ,1): ['I 41/a S'],
             (88 ,2): ['I 41/a Z', 'I 41/a Z1'],
             (90 ,1): ['P 4 21 2', 'C 4 2 21' ],  ## TODO: what is "C 4 2 21"
             (91 ,1): ['P 41 2 2'],
             (92 ,1): ['P 41 21 2'],
             (94 ,1): ['P 42 21 2'],
             (95 ,1): ['P 43 2 2'],
             (96 ,1): ['P 43 21 2'],
             (98 ,1): ['I 41 2 2'],
             (101,1): ['P 42 c m'],
             (102,1): ['P 42 n m'],
             (105,1): ['P 42 m c'],
             (106,1): ['P 42 b c'],
             (109,1): ['I 41 m d'],
             (110,1): ['I 41 c d'],
             (113,1): ['P -4 21 m', 'C -4 m 21'],  ## TODO: what is "C -4 m 21" ?
             (114,1): ['P -4 21 c'],
             (117,1): ['C -4 2 b'],                ## TODO: what is "C -4 2 b"
             (123,1): ['P 4/m m m'],
             (122,1): ['F -4 d 2'],                ## TODO: what is "F -4 d 2"
             (124,1): ['P 4/m c c', 'C 4/m c c'],  ## TODO: what is "C 4/m c c"
             (125,1): ['P 4/n b m S'],
             (125,2): ['P 4/n b m Z'],
             (126,1): ['P 4/n n c S'],
             (126,2): ['P 4/n n c Z'],
             (127,1): ['P 4/m b m'],
             (128,1): ['P 4/m n c'],
             (129,1): ['P 4/n m m S', 'P 4/n m m'],
             (129,2): ['P 4/n m m Z'],
             (130,1): ['P 4/n c c S'],
             (130,2): ['P 4/n c c Z'],
             (131,1): ['P 42/m m c'],
             (132,1): ['P 42/m c m'],
             (133,1): ['P 42/n b c S'],
             (133,2): ['P 42/n b c Z'],
             (134,1): ['P 42/n n m S'],
             (134,2): ['P 42/n n m Z'],
             (135,1): ['P 42/m b c'],
             (136,1): ['P 42/m n m'],
             (137,1): ['P 42/n m c S'],
             (137,2): ['P 42/n m c Z'],
             (138,1): ['P 42/n c m S'],
             (138,2): ['P 42/n c m Z'],
             (139,1): ['I 4/m m m', 'F 4/m m m'],        ## TODO: what is "F 4/m m m"
             (140,1): ['I 4/m c m', 'F 4/m m c'],        ## TODO: what is "F 4/m m c"
             (141,1): ['I 41/a m d S'],
             (141,2): ['I 41/a m d Z', 'F 41/d d m Z'],  ## TODO: what is "F 41/d d m Z"
             (142,1): ['I 41/a c d S', 'F 41/a d c'],    ## TODO: what is "F 41/a d c"
             (142,2): ['I 41/a c d Z'],
             (167,2): ['R -3 c R' ],
             (198,1): ['P 21 3'   ],
             (199,1): ['I 21 3'   ],
             (200,1): ['P m -3'   ],
             (201,1): ['P n -3 S' ],
             (201,2): ['P n -3 Z' ],
             (202,1): ['F m -3'   ],
             (203,1): ['F d -3 S' ],  ## untested !
             (203,2): ['F d -3 Z' ],  ## untested !
             (204,1): ['I m -3'   ],
             (205,1): ['P a -3'   ],
             (206,1): ['I a -3'   ],
             (208,1): ['P 42 3 2' ],
             (210,1): ['F 41 3 2' ],
             (212,1): ['P 43 3 2' ],
             (213,1): ['P 41 3 2' ],
             (214,1): ['I 41 3 2' ],
             (221,1): ['P m -3 m' ],
             (222,1): ['P n -3 n S' ], ## untested !
             (222,2): ['P n -3 n Z' ], ## untested !
             (223,1): ['P m -3 n' ],
             (224,1): ['P n -3 m S'], ## untested !
             (224,2): ['P n -3 m Z'], ## untested !
             (225,1): ['F m -3 m' ],
             (226,1): ['F m -3 c' ],
             (227,1): ['F d -3 m S' ],
             (227,2): ['F d -3 m Z' ],
             (228,1): ['F d -3 c S' ], ## untested !
             (228,2): ['F d -3 c Z' ], ## untested !
             (229,1): ['I m -3 m' ],
             (230,1): ['I a -3 d' ], }
    #syns = { 'I 4/m 2/c 2/m' : ['I 4/m c m'] }  ## this is mainly for ICSD (ICSD use slightly different notation for groups)
    genr = None   ## all matrices for generators

    def __init__( self, num, snum ):
        self.num  = num
        self.snum = snum
        self.mydata = self.data[ self.num-1 ][ self.snum-1 ]

        self.gens = list( self.mydata['gens'] )

        e_op = ( 0, (0.0, 0.0, 0.0) )  ## identical with Mat( 1,0,0, 0,1,0, 0,0,1 )
        e_in = ( 1, (0.0, 0.0, 0.0) )  ## inversion with Mat(-1,0,0, 0,-1,0, 0,0,-1 )
        if e_op not in self.gens:
            self.gens.append( e_op )

        self.gens.reverse()
        if self.mydata['inv'] and e_in not in self.gens:
            self.gens.append( e_in )


    def __len__( self ):
        return len( self.gens )

    def __getattr__( self, n ):
        if n not in self.__dict__:
            if 'mydata' not in self.__dict__ or n not in self.mydata:
                raise AttributeError, "can't found attribute"
            return self.mydata[ n ]
        else:
            return self.__dict__[ n ]

    def __getitem__( self, n ):
        e = self.gens[ n ]
        m = self.genr[ e[0] ]
        t =  Vec( *e[1] )
        return ( m, t )

    def __hash__( self ):
        return hash( ( self.num, self.snum ) )

    def __eq__( self, other ):
        return self.num == other.num and self.snum == other.snum

    @classmethod
    def subs( klas, num ):
        return xrange( 1, len( klas.data[ num-1 ] ) + 1 )

    @classmethod
    def from_symb( klas, symb ):
        for n, gs in enumerate( klas.data ):
            for sn, g in enumerate( gs ):
                if g['symb'] == symb:
                    return SpGrp( n + 1, sn + 1 )

                ## test for synonyms...
                for n_sn, ss in klas.syns.iteritems():
                    if symb in ss:
                        return SpGrp( n_sn[ 0 ], n_sn[ 1 ] )

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
             }
        if typ in vs:
            return vs[ typ ]
        elif typ == 'R':
            if self.snum == 2:
                return []
            elif self.snum == 1:
                return [ Vec( 2/3.0, 1/3.0, 1/3.0 ), Vec( 1/3.0, 2/3.0, 2/3.0 ) ]


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

if not SpGrp.data:
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
    s2 = SpGrp( 225, 1 )
    print id( s ), id( s2 )
    print s == s2
    exit( 0 )
    print len( s * Vec( 0.25, 0.25, 0.25 ) )

    l = set()
    for g in SpGrp.data:
        for sg in g:
            l.add( sg['symb'][0] )

    print l
