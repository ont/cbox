import sys
from vec import *
from ucell import *

def stdlines():
    l = sys.stdin.readline()
    while l:
        l = l.strip()
        if l and l[ 0 ] != '#':
            yield l
        l = sys.stdin.readline()


def str2vec( s ):
    return Vec( *map( float, s.split() ) )


def lines2cell( rep, ls ):
    """ rep: reper for unit cell
        ls : unparsed lines "[atom name] [x] [y] [z]"
    """
    u = UCell( rep )
    atoms = {}
    for l in ls:
        ps = l.split()
        xyz = map( float, ps[ 1: ] )
        name = ps[ 0 ]
        if name in atoms:
            atoms[ name ].append( Vec( *xyz ) )
        else:
            atoms[ name ] = [ Vec( *xyz ) ]

    for name, pnts in atoms.iteritems():
        u.add( name, pnts )

    return u
