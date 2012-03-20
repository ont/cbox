from ipe  import *
from vec  import *
from mat  import *
from math import *

#from xml import etree as ET
from xml.etree import ElementTree as ET



class DrawIPE( object ):
    def __init__( self ):
        self.pos = Vec( 0,0,0 )  ## position for trans
        self.ipe = Painter()
        self.grp = None          ## for usage in self.save
        self.objs      = [[], ]  ## generic objects to draw
        self.objs_ipe  = [[], ]  ## object which are rendered only by ipe drawer
        self.objs_burn = [[], ]  ## burned object (it doesn't need rendering


    def setup( self, al, th, dist, ang = 40 ):
        self.al, self.th, self.tg = al, th, tan( ang * pi / 180.0 )
        self.dist = dist
        self.ortho = False


    def setup_plane( self, p, d ):
        self.dist = p.r.vlen() + d
        n = p.n
        self.th =  atan2( n.z, sqrt( n.x**2 + n.y**2 ) ) + pi / 2
        self.al = -atan2( n.y, n.x )
        self.ortho = True


    def setup_drawgl( self, drawgl ):
        self.setup( drawgl.gl.alpha * pi / 180, drawgl.gl.theta * pi / 180, drawgl.gl.dist )


    def proj( self, v ):
        m_y = Mat(  cos( -self.al ) ,  0, sin( -self.al ),
                    0               ,  1, 0              ,
                   -sin( -self.al ) ,  0, cos( -self.al ) )

        m_x = Mat( 1,  0               , 0                ,
                   0,  cos( -self.th ) , -sin( -self.th ) ,
                   0,  sin( -self.th ) ,  cos( -self.th ) )

        v = v + self.pos
        v = m_y * v
        v = m_x * v
        v.z += self.dist

        if self.ortho:
            return v
        else:
            return Vec( v.x/v.z * 400 / self.tg, v.y/v.z * 400 / self.tg, v.z )



    def trans( self, v ):
        self.pos += v


    def group( self ):
        """ Create new group to add to when self.__call__
        """
        if self.objs[ -1 ]:
            self.objs.append( [] )
        if self.objs_ipe[ -1 ]:
            self.objs_ipe.append( [] )
        if self.objs_burn[ -1 ]:
            self.objs_burn.append( [] )


    def line( self, v1, v2, color, **opt ):
        v1 = self.proj( v1 )
        v2 = self.proj( v2 )
        s = Span( Mark( v1 ), Mark( v2 ) )
        s.color = " ".join( map( lambda a: str( 1-a ), color ) )
        s.width  = opt.get( 'width', 'normal' )
        s.style  = opt.get( 'style', None     )
        self.grp.add( s )


    def sphere( self, pos, r, color, **opt ):
        pos = self.proj( pos )
        #r = r/( pos.z + self.dist ) * 200 / self.tg
        c = Circle( pos, 10 * r )
        c.color = " ".join( map( lambda a: str( a ), color ) )
        c.width = opt.get( 'width', 'normal' )
        c.style = 'dashed' if opt.get( 'invis', False ) else 'normal'
        self.grp.add( c )

    def text( self, pos, txt ):
        pos = self.proj( pos )
        l = Label( pos, txt )
        self.grp.add( l )


    def __call__( self, obj, **opt ):
        if type( obj ) is str and 'pos' in opt:
            pos = self.proj( opt['pos'] )
            self.objs_burn[-1].append( Label( pos, obj ) )
            return

        if not hasattr( obj, 'draw' ) and not hasattr( obj, 'draw_ipe' ):
            raise Exception, "Object %s can't be drawn" % obj

        optt = dict( getattr( obj, 'opt', {} ) )  ## take a copy of default values
        optt.update( opt )                        ## change default values
        obj.opt = optt                            ## save it to object

        if hasattr( obj, 'draw' ):         ## this obj use standart API
            self.objs[-1].append( obj )

        if hasattr( obj, 'draw_ipe' ):     ## obj use special ipe featrues
            self.objs_ipe[-1].append( obj )


    def clear( self ):
        self.objs      = [[], ]
        self.objs_ipe  = [[], ]
        self.objs_burn = [[], ]


    def save( self, fname ):
        self.ipe.objs = []  ## clear 2D objects

        for g in self.objs: ## for each group...
            self.grp = Group()

            for o in g:     ## for each object in group
                self.pos = Vec( 0,0,0 )
                o.draw( self )  ## draw with api

            ## z-order sorting (draw first with greater z-value)
            def depth( x ):
                if hasattr( x, 'pos' ):
                    return x.pos.z
                elif type( x ) is Span:
                    vm = 0.5 * ( x.m1.pos + x.m2.pos )
                    return vm.z
                else:
                    return 100000

            self.grp.objs.sort( key = depth, reverse = True )

            self.ipe.objs.append( self.grp ) ## send created group to ipe

        if self.objs_burn != [[],]:
            for g in self.objs_burn:  ## simply add already rendered objects to tree
                grp = Group()
                for o in g:
                    grp.add( o )
                self.ipe.objs.append( grp ) ## send created group to ipe

        for g in self.objs_ipe:
            for o in g:
                o.draw( self.ipe )  ## obj save to root by self

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
