from numpy import mat, matrix
from math  import sin, cos, sqrt
from lxml  import etree as ET


class Mark( object ):
    """ A simple point.
    """
    def __init__( self, pos ):
        self.pos = pos
        self.style = None
        self.visible = True


    def saveXML( self, root_node ):
        """ Save self to root XML node.
        """
        if not self.visible:
            return
        use = ET.SubElement( root_node, "use" )
        use.set( "name", "mark/disk(sx)" )
        use.set( "pos", "%f %f" % ( self.pos[ 0 ], self.pos[ 1 ] ) )
        use.set( "size", "normal" )
        use.set( "stroke", "black" )


class Circle( object ):
    """ Basic-solid cirlce.
    """
    def __init__( self, pos, r ):
        self.color = "black"
        self.pos = pos
        self.r = r

    def saveXML( self, root ):
        path = ET.SubElement( root, "path" )
        path.set( "stroke", self.color )
        path.set( "layer", "alpha" )
        path.text = "%s 0 0 %s %s %s e" % ( self.r, self.r, self.pos[ 0 ], self.pos[ 1 ] )



class Span( object ):
    """ A simple line between two dots.
        Each dot can be drawn too.
    """
    def __init__( self, m1, m2 ):
        self.m1 = m1
        self.m2 = m2
        self.m1.visible = False  # don't draw endpoints on Span by default
        self.m2.visible = False
        self.style = None  # can be dashed, solid ...
        self.color = 'black'
        self.width = 'normal'


    def saveXML( self, root_node ):
        """ Save self to root XML node.
        """
        path = ET.SubElement( root_node, "path" )
        path.set( "stroke", self.color )
        path.set( "pen", self.width )
        if self.style is not None:
            path.set( "dash", self.style )

        text =  "%f %f m\n" % ( self.m1.pos[ 0 ], self.m1.pos[ 1 ] )
        text += "%f %f l\n" % ( self.m2.pos[ 0 ], self.m2.pos[ 1 ] )
        path.text = text


class Group( object ):
    """ Class for grouping ipe objects
    """
    def __init__( self ):
        self.objs = []  ## objects in group

    def add( self, obj ):
        self.objs.append( obj )

    def saveXML( self, root ):
        grp = ET.SubElement( root, "group" )
        for o in self.objs:
            o.saveXML( grp )



class Painter( object ):
    """ Class for saving objects into XML file.
    """
    def __init__( self, objs = None ):
        self.objs = []
        if objs is not None:
            self.objs = objs


    def saveTo( self, fname ):
        """Write each XML representation of object to file
        """
        root = ET.Element("ipe")
        root.set( "version", "70007" )
        root.set( "creator", "cbox" )

        style = ET.SubElement( root, "ipestyle" )
        style.set( "name", "basic" )
        dash = ET.SubElement( style, "dashstyle" )
        dash.set( "name", "dashed" )
        dash.set( "value", "[4] 0" )

        color = ET.SubElement( style, "color" )
        color.set( "name", "black" )
        color.set( "value", "0 0 0" )

        page = ET.SubElement( root, "page" )

        ET.SubElement( page, "layer" ).set( "name", "alpha" )

        view = ET.SubElement( page, "view" )
        view.set( "layers", "alpha" )
        view.set( "active", "alpha" )

        for o in self.objs:
            o.saveXML( page )

        tree = ET.ElementTree( root )
        tree.write( fname, pretty_print = True )



