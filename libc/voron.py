import sys
from vec        import *
from reper      import *
from mesh       import *
from subprocess import Popen, PIPE

import reper_min


class Voron( object ):
    def __init__( self, v1, v2, v3, pos = Vec( 0,0,0 ) ):
        self.rep = Reper( v1, v2, v3 )
        self.pos = pos
        self.update()

    def update( self, qhalf = "qhalf", qconvex = "qconvex" ):
        """ Update mesh for new self.v*
        """

        def makeDots( v1, v2, v3 ):
            """ helper function
            """
            res = []
            for nx in xrange( -2, 3 ):
                for ny in xrange( -2, 3 ):
                    for nz in xrange( -2, 3 ):
                        res.append( ( v1 * nx )  + ( v2 * ny )  + ( v3 * nz ) )
            return res

        def str2vec( s ):
            """ helper function
            """
            if ',' in s:
                ss = s.split( "," )
            else:
                ss = s.split( )

            fs = map( lambda s: float( s.strip( ) ), ss )
            return Vec( fs[ 0 ], fs[ 1 ], fs[ 2 ] )


        rep = self.rep.minimize()

        try:
            dots = makeDots( rep.v1, rep.v2, rep.v3 )

            if 'win' in sys.platform:
                p1 = Popen( [ qhalf, "Fp" ], stdin = PIPE, stdout = PIPE ) #, close_fds = True )
                p2 = Popen( [ qconvex, "o" ],stdin = PIPE, stdout = PIPE ) #, close_fds = True )
            else:
                p1 = Popen( [ qhalf, "Fp" ], stdin = PIPE, stdout = PIPE, close_fds = True )
                p2 = Popen( [ qconvex, "o" ],stdin = PIPE, stdout = PIPE, close_fds = True )


            s  = '3 1\n'
            s += '0 0 0\n'
            s += '4\n'
            s += str( len( dots ) - 1 ) + '\n'
            for d in dots:
                if d.vlen() > 0.001:
                    n   = d.norm()
                    off = - d.vlen() / 2.0
                    s += "%.20f %.20f %.20f %.20f\n" % ( n[ 0 ], n[ 1 ], n[ 2 ], off )

            ret = p1.communicate( s )[ 0 ]
            ret = p2.communicate( ret )[ 0 ]

            lines  = ret.split( '\n' )
            params = lines[ 1 ].split( )
            params = map( lambda s: int( s.strip() ), params )
            dcount = params[ 0 ]

            lines = lines[ 2: ]
            pnts = map( lambda s: str2vec( s ), lines[ :dcount ] )

            lines = lines[ dcount: ]

            polys = []
            for l in lines:
                nums = l.split()
                if nums:
                    nums = map( lambda s: int( s ), nums )
                    nums = nums[ 1: ]
                    ppnt = map( lambda n: pnts[ n ], nums )
                    polys.append( Poly( ppnt ) )
        except Exception, e:
            print "errrrrorrr:", e

        self.mesh =  Mesh( polys )

    def __repr__( self ):
        return str( self.mesh )
