import sys
from vec    import *
from reper  import *
from ucell  import *

def stdlines():
    l = sys.stdin.readline()
    while l:
        l = l.strip()
        if l and l[ 0 ] != '#':
            yield l
        l = sys.stdin.readline()


def str2vec( s ):
    return Vec( *map( float, s.split() ) )

def vec2str( v ):
    return "%s %s %s" % tuple( v )


def lines2cell( ls ):
    """ rep: reper for unit cell
        ls : unparsed lines "[atom name] [x] [y] [z]"
    """
    v1 = str2vec( ls[ 0 ] )
    v2 = str2vec( ls[ 1 ] )
    v3 = str2vec( ls[ 2 ] )

    rep = Reper( v1, v2, v3 )

    u = UCell( rep )
    ats = {}
    for l in ls[ 3: ]:
        ps = l.split()
        xyz = map( float, ps[ 1: ] )
        name = ps[ 0 ]

        v = Vec( *xyz )

        if name in ats:
            ats[ name ].append( v )
        else:
            ats[ name ] = [ v ]

    for name, atoms in ats.iteritems():
        u.add( name, atoms )

    return u


def cell2lines( u ):
    s = "%s\n%s\n%s\n\n" % tuple( map( vec2str, u.rep ) )
    for name, ats in u.atoms.iteritems():
        s += "\n".join( map( lambda a: "%s %s" % ( name, vec2str( a ) ), ats ) )
        s += "\n"

    return s




def lines2cells( ls ):
    def split( ls ):
        res = []
        for l in ls:
            if l != "<<< END":
                res.append( l )
            else:
                yield res
                res = []
        yield res


    res = []
    for g in split( ls ):  ## for each group of lines in ls...
        res.append( lines2cell( g ) )

    return res

