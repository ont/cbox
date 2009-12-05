
class Sort( object ):
    def __init__( self, name ):
        self.name = name

    def __eq__( self, other ):
        return self.name == other.name

    def __hash__( self ):
        return 1

    def __repr__( self ):
        return "Sort( %s )" % self.name



