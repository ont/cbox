class Atom( object ):
    def __init__( self, name, pos ):
        self.name = name
        self.pos = pos

    def __repr__( self ):
        return "Atom( '%s', %s, %s, %s )" % ( self.name, self.pos.x, self.pos.y, self.pos.z )
