from vec  import Vec
from mesh import Poly


def draw( self, api ):
    visible = set()

    apnts = [ d for p in self.polys for d in p.pnts ]
    cv = reduce( lambda a,b: a+b, apnts )
    cv = 1 / len( apnts ) * cv

    cv = api.proj( cv )

    for i,p in enumerate( self.polys ):
        pnts = p.pnts[ 0:3 ]
        pnts = map( api.proj, pnts )  ## project all points
        p_temp = Poly( pnts )
        n_temp = p_temp.norm( bvec = cv )

        if n_temp[ 2 ] < 0:
            visible.update( p.edgs )

    for e in self.uedgs:
        if e in visible:
            api.line( e.p1, e.p2, self.opt['color'] )
        else:
            api.line( e.p1, e.p2, ( 0.3, 0.3, 0.3 ), style = 'dashed' )


import mesh
mesh.Mesh.draw= draw
mesh.Mesh.opt = { 'color' : ( 1,1,1 ) }
