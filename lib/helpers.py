def groupby( l, cnt ):
    for i in xrange( len( l ) / cnt ):
        yield tuple( l[ cnt * i : cnt * ( i + 1 ) ] )
