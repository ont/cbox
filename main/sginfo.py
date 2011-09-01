#!/usr/bin/env python2
import sys
sys.path.extend( [ '../lib', '../liba', '../libc' ] )

from spgrp import *

if len( sys.argv ) < 3:
    print "Usage: spinfo.py [num], [snum]"
    exit( 1 )

s = SpGrp( *map( int, sys.argv[ 1: ] ) )
print s
print s.mydata
print 'cvecs:', s.cvecs()
