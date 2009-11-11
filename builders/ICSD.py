import re
from builder  import *
from vec      import *
from atom     import *
from ucell    import *
from spgrp    import *

class BICSD( Builder ):
    __name__ = 'ICSD importer'
    __input__ = { 'fname' : str }

    def __init__( self ):
        self.info  = {}
        self.ucell = []
        self.basis = []
        self.spgrp = None
        self.SGR_dict()  ## load and prepare convert dictionary
                         ## for space groups


    def prep( self, l ):
        return ' '.join( l.strip().split() )


    def tick( self, l ):
        """Check for new section in ICSD file
           Return True if line starts new one.
        """
        ps = l.split()
        if ps[ 0 ] in ( 'COL', 'DATE', 'NAME', 'FORM', 'TITL', 'REF', 'AUT', 'CELL', 'SGR', 'CLAS', 'PRS', 'ANX', 'PARM', 'WYCK', 'TF', 'RVAL', 'TEST' ):
            self.section = ps[ 0 ]
            return True
        return False


    def COL( self, l ):
        exp = re.compile( r'\D+(\d+)' )
        self.info['id'] = exp.search( l ).group( 1 )


    def FORM( self, l ):
        exp = re.compile( r'FORM (.*)$' )
        res = exp.search( l )
        if res:
            self.info['form'] = res.group( 1 )


    def CELL( self, l ):
        exp = re.compile( r'CELL\s+a\s*=(\S+)\s+b\s*=(\S+)\s+c\s*=(\S+)\s+\S\s*=(\S+)\s+\S\s*=(\S+)\s+\S\s*=(\S+)' )
        res = exp.search( l )
        if res:
            gs = res.groups()
            gs = map( lambda g: float( g.replace( '(', '' ).replace( ')', '' ) ), gs )
            self.ucell = UCell( *( gs[ 0:3 ] + gs[ 3:6 ] ) )


    def PARM( self, l ):
        if 'PARM' not in l:
            ps = l.split()
            xyz = map( lambda s: float( s.replace( '(', '' ).replace( ')', '' ) ), ps[ 4:7 ] )
            a = Atom( ps[ 0 ], Vec( *xyz ) )
            self.basis.append( a )


    def SGR( self, l ):
        exp = re.compile( r'SGR\s+(.+)\s+\(\d+\)' )
        res = exp.search( l )
        if res:
            num, snum =  *self.conv[ res.group( 1 ) ]
            self.spgrp = SpGrp( num-1, snum-1 )


    def SGR_dict( self ):
        """ Prepare conversion dictionary.
        """
        ls = open( 'ICSDKONV.DAT' ).readlines()
        num = None
        self.conv = {}
        for l in ls:
            if l[ 0:4 ] == 'spgr':
                num = int( l.split( '=' )[ 1 ] )
            elif l.strip():
                p = l.split()
                snum = int( p[ 0 ] )
                self.conv[ ' '.join( p[ 1: ] ) ] = ( num, snum )


    def build( self, **kargs ):
        fname = kargs[ 'fname' ]
        lines = open( fname ).readlines( )
        lines = map( self.prep, lines )
        for l in lines:
            self.tick( l )
            if hasattr( self, self.section ):
                getattr( self, self.section )( l )

        print self.ucell
        print self.spgrp
        print self.basis



if __name__  ==  "__main__":
    b = BICSD( )
    b.build( fname = 'TEI.TXT' )
