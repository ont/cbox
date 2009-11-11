import pickle
import re
from helpers  import groupby

def sg( ls ):
    res, n = [], 0
    for l in ls:
        if 'spgr' in l:
            if n > 0:
                yield res
            res, n = [], n + 1
        if n > 0:
            res.append( l.strip() )
    yield res

ls = open( 'spgrp.dat' ).readlines()
ls = ls[ 235: ]   ## drop conversion data

exp = re.compile( r'^spgr\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.*)$' )

data = [ [] for i in xrange( 230 ) ]

for s in sg( ls ):
    res = exp.match( s[ 0 ] )
    if res:
        num, snum, laue, inv, ngp, nsp, ngen = map( int, res.groups()[:-1] )
        symb = res.groups()[ -1 ]

        wyck = list( groupby( map( int, s[ 2 ].split() ), 2 ) )

        gens = []
        for l in filter( lambda l: l, s[ 3: ] ):
            ps = l.split()
            n = int( ps[ 0 ] )
            v = tuple( map( float, ps[ 1: ] ) )
            gens.append( ( n, v ) )

        gens.reverse()

        ginf = dict( laue  = laue,
                     inv   = inv,
                     ngp   = ngp,
                     #nsp   = nsp,
                     #ngen  = ngen,
                     symb  = symb,
                     rcnd  = s[ 1 ],
                     wyck  = wyck,
                     gens  = gens )
        data[ num-1 ].append( ginf )


f = open( 'spgrp.pkl', 'wb' )
pickle.dump( data, f, -1 )
f.close()
