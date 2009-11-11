import mat
import mat_ident

def is_ortho( self ):
    """ Test for orthogonality
    """
    if ( self.t() * self ).is_ident():
        return True
    else:
        return False

mat.Mat.is_ortho = is_ortho
