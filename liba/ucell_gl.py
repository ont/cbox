import vec_gl

from vec import *

import ucell
ucell.UCell.clrs = {
    "A"   :  ( 255 , 0   , 0   ),
    "B"   :  ( 0   , 255 , 0   ),
    "H"   :  ( 198 , 39  , 227 ),
    "He"  :  ( 104 , 116 , 143 ),
    "Li"  :  ( 192 , 140 , 76  ),
    "Be"  :  ( 16  , 167 , 91  ),
    "B"   :  ( 79  , 237 , 64  ),
    "C"   :  ( 131 , 48  , 54  ),
    "N"   :  ( 253 , 226 , 91  ),
    "O"   :  ( 93  , 19  , 212 ),
    "F"   :  ( 223 , 191 , 8   ),
    "Ne"  :  ( 70  , 156 , 93  ),
    "Na"  :  ( 173 , 85  , 4   ),
    "Mg"  :  ( 84  , 44  , 75  ),
    "Al"  :  ( 40  , 24  , 64  ),
    "Si"  :  ( 180 , 107 , 42  ),
    "P"   :  ( 244 , 224 , 246 ),
    "S"   :  ( 200 , 142 , 27  ),
    "Cl"  :  ( 14  , 254 , 218 ),
    "Ar"  :  ( 87  , 61  , 72  ),
    "K"   :  ( 0   , 14  , 190 ),
    "Ca"  :  ( 138 , 128 , 250 ),
    "Sc"  :  ( 228 , 198 , 87  ),
    "Ti"  :  ( 230 , 7   , 231 ),
    "V"   :  ( 102 , 209 , 180 ),
    "Cr"  :  ( 188 , 67  , 47  ),
    "Mn"  :  ( 79  , 193 , 252 ),
    "Fe"  :  ( 158 , 166 , 84  ),
    "Co"  :  ( 139 , 157 , 168 ),
    "Ni"  :  ( 247 , 126 , 66  ),
    "Cu"  :  ( 172 , 164 , 4   ),
    "Zn"  :  ( 23  , 194 , 96  ),
    "Ga"  :  ( 106 , 57  , 174 ),
    "Ge"  :  ( 33  , 144 , 75  ),
    "As"  :  ( 19  , 87  , 179 ),
    "Se"  :  ( 111 , 166 , 23  ),
    "Br"  :  ( 110 , 184 , 158 ),
    "Kr"  :  ( 70  , 40  , 244 ),
    "Rb"  :  ( 188 , 109 , 26  ),
    "Sr"  :  ( 203 , 90  , 246 ),
    "Y"   :  ( 18  , 11  , 118 ),
    "Zr"  :  ( 105 , 153 , 182 ),
    "Nb"  :  ( 108 , 193 , 200 ),
    "Mo"  :  ( 219 , 114 , 165 ),
    "Tc"  :  ( 108 , 232 , 127 ),
    "Ru"  :  ( 68  , 99  , 181 ),
    "Rh"  :  ( 243 , 65  , 17  ),
    "Pd"  :  ( 217 , 30  , 209 ),
    "Ag"  :  ( 237 , 102 , 175 ),
    "Cd"  :  ( 168 , 90  , 20  ),
    "In"  :  ( 226 , 31  , 208 ),
    "Sn"  :  ( 221 , 146 , 242 ),
    "Sb"  :  ( 229 , 101 , 71  ),
    "Te"  :  ( 235 , 208 , 132 ),
    "I"   :  ( 110 , 13  , 239 ),
    "Xe"  :  ( 231 , 224 , 241 ),
    "Cs"  :  ( 95  , 214 , 44  ),
    "Ba"  :  ( 179 , 206 , 232 ),
    "Hf"  :  ( 25  , 208 , 13  ),
    "Ta"  :  ( 79  , 26  , 196 ),
    "W"   :  ( 103 , 108 , 18  ),
    "Re"  :  ( 232 , 146 , 177 ),
    "Os"  :  ( 239 , 34  , 185 ),
    "Ir"  :  ( 225 , 128 , 214 ),
    "Pt"  :  ( 81  , 201 , 178 ),
    "Au"  :  ( 48  , 217 , 212 ),
    "Hg"  :  ( 163 , 3   , 14  ),
    "Tl"  :  ( 46  , 193 , 223 ),
    "Pb"  :  ( 108 , 33  , 62  ),
    "Bi"  :  ( 35  , 30  , 159 ),
    "Po"  :  ( 3   , 248 , 190 ),
    "At"  :  ( 144 , 192 , 254 ),
    "Rn"  :  ( 29  , 179 , 188 ),
    "Fr"  :  ( 202 , 3   , 178 ),
    "Ra"  :  ( 168 , 165 , 166 ),
    "Rf"  :  ( 218 , 234 , 79  ),
    "Db"  :  ( 116 , 185 , 188 ),
    "Sg"  :  ( 110 , 211 , 98  ),
    "Bh"  :  ( 57  , 115 , 212 ),
    "Hs"  :  ( 167 , 109 , 205 ),
    "Mt"  :  ( 80  , 39  , 225 ),
    "Ds"  :  ( 26  , 248 , 243 ),
    "Rg"  :  ( 3   , 7   , 6   ),
    "Uub" :  ( 31  , 117 , 71  ),
    "Uut" :  ( 46  , 53  , 176 ),
    "Uuq" :  ( 178 , 104 , 53  ),
    "Uup" :  ( 145 , 7   , 77  ),
    "Uuh" :  ( 8   , 49  , 5   ),
    "Uus" :  ( 141 , 87  , 161 ),
    "Uuo" :  ( 154 , 38  , 182 ),
    "La"  :  ( 210 , 242 , 124 ),
    "Ce"  :  ( 210 , 241 , 17  ),
    "Pr"  :  ( 231 , 42  , 84  ),
    "Nd"  :  ( 122 , 28  , 235 ),
    "Pm"  :  ( 37  , 135 , 12  ),
    "Sm"  :  ( 18  , 203 , 108 ),
    "Eu"  :  ( 35  , 204 , 139 ),
    "Gd"  :  ( 7   , 129 , 102 ),
    "Tb"  :  ( 61  , 126 , 32  ),
    "Dy"  :  ( 210 , 86  , 182 ),
    "Ho"  :  ( 212 , 238 , 15  ),
    "Er"  :  ( 97  , 68  , 108 ),
    "Tm"  :  ( 81  , 74  , 137 ),
    "Yb"  :  ( 58  , 44  , 245 ),
    "Lu"  :  ( 16  , 166 , 243 ),
    "Ac"  :  ( 213 , 189 , 54  ),
    "Th"  :  ( 142 , 100 , 191 ),
    "Pa"  :  ( 236 , 55  , 60  ),
    "U"   :  ( 151 , 67  , 125 ),
    "Np"  :  ( 110 , 246 , 44  ),
    "Pu"  :  ( 12  , 180 , 183 ),
    "Am"  :  ( 237 , 165 , 82  ),
    "Cm"  :  ( 93  , 255 , 79  ),
    "Bk"  :  ( 192 , 219 , 33  ),
    "Cf"  :  ( 119 , 183 , 4   ),
    "Es"  :  ( 14  , 211 , 93  ),
    "Fm"  :  ( 93  , 198 , 87  ),
    "Md"  :  ( 192 , 191 , 179 ),
    "No"  :  ( 125 , 211 , 35  ),
    "Lr"  :  ( 16  , 29  , 157 ),
    "D"   :  ( 34  , 82  , 200 ),
}

def draw( self, api ):
    v0 = Vec( 0.0, 0.0, 0.0 )
    api.line( v0, self.rep.v1, (1,1,1) )
    api.line( v0, self.rep.v2, (1,1,1) )
    api.line( v0, self.rep.v3, (1,1,1) )

    for name, vecs in self.atoms.iteritems():
        for v in vecs:
            color = map( lambda c: c/255.0, self.clrs.get( name, (255,255,255) ) )
            api.sphere( v, 0.03, color  )

ucell.UCell.draw = draw
