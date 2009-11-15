from ipe  import *
from vec  import *
from math import *

from lxml import etree as ET


class DrawIPE( object ):
    def __init__( self ):
        self.pos = Vec( 0,0,0 )  ## position for trans
        self.ipe = Painter()
        self.objs     = []
        self.objs_ipe = []


    def setup( self, al, th, dist, ang = 40 ):
        self.al, self.th, self.tg = al, th, tan( ang * pi / 180.0 )
        self.dist = dist


    def setup_plane( self, p, d ):
        self.dist = p.r.vlen() + d
        n = p.n
        self.th =  atan2( n.z, sqrt( n.x**2 + n.y**2 ) ) + pi / 2
        self.al = -atan2( n.y, n.x )
        self.ortho = True


    def proj( self, v ):
        c_al = cos( self.al )
        s_al = sin( self.al )
        c_th = cos( self.th )
        s_th = sin( self.th )

        x,y,z = list( v + self.pos )
        xn = c_al*x - s_al*y
        yn = c_th*( c_al*y + s_al*x ) - s_th*z
        zn = c_th*z + s_th*( c_al*y + s_al*x ) + self.dist

        xn = c_al * c_th * x - s_al * c_th * y + s_th * z
        yn = s_al * x + c_al * y
        zn = -c_al * s_th * x + s_al * s_th * y + c_th * z + self.dist


        if self.ortho:
            return Vec( xn, yn, zn )
        else:
            return Vec( xn/zn * 200 / self.tg, yn/zn * 200 / self.tg, zn )


    def trans( self, v ):
        self.pos += v


    def line( self, v1, v2, color, **opt ):
        v1 = self.proj( v1 )
        v2 = self.proj( v2 )
        s = Span( Mark( v1 ), Mark( v2 ) )
        s.color = " ".join( map( lambda a: str( 1-a ), color ) )
        s.width  = opt.get( 'width', 'normal' )
        s.style  = opt.get( 'style', None     )
        self.ipe.objs.append( s )


    def sphere( self, pos, r, color, **opt ):
        pos = self.proj( pos )
        #r = r/( pos.z + self.dist ) * 200 / self.tg
        c = Circle( pos, r )
        c.color = " ".join( map( lambda a: str( 1-a ), color ) )
        self.ipe.objs.append( c )


    def __call__( self, obj, **opt ):
        if not hasattr( obj, 'draw' ) and not hasattr( obj, 'draw_ipe' ):
            raise Exception, "Object %s can't be drawn" % obj

        optt = dict( getattr( obj, 'opt', {} ) )  ## take a copy of default values
        optt.update( opt )                        ## change default values
        obj.opt = optt                            ## save it to object

        if hasattr( obj, 'draw' ):         ## this obj use standart API
            self.objs.append( obj )

        if hasattr( obj, 'draw_ipe' ):     ## obj use special ipe featrues
            self.objs_ipe.append( obj )


    def clear( self ):
        self.objs     = []
        self.objs_ipe = []


    def save( self, fname ):
        self.ipe.objs = []  ## clear 2D objects

        for o in self.objs:
            self.pos = Vec( 0,0,0 )
            o.draw( self )  ## draw with api

        for o in self.objs_ipe:
            o.draw( page )  ## obj save to root by self

        self.ipe.saveTo( fname )


#<?xml version="1.0"?>
#<!DOCTYPE ipe SYSTEM "ipe.dtd">
#<ipe version="70007" creator="Ipe 7.0.7">
#<page>
#<layer name="alpha"/>
#<view layers="alpha" active="alpha"/>
#<text matrix="1 0 0 1 29.8334 -49.1008" transformations="translations" pos="46.1585 71.9837" stroke="black" type="label" width="8.583" height="4.294" depth="1.49" valign="baseline">$a_i$</text>
#</page>
#</ipe>




drawipe = DrawIPE()
