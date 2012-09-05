What is this ?
==============
Easy to use python classes for working with crystallographic objects (space groups, unit cells, sorts, Zelling symbols).
Main goal of this project is to provide some sandbox where you can easily build/draw/manipulate with unit cells & sorts.

Some features:
  * modularity -- i.e. basic classes with minimum functionality and 'aspects' which is 'plugged' into basic objects.
  * basic math objects: `Vec`, `Mat`, `Reper` with overloaded operations `+ - * /` and related math operations.
  * basic geom objects: `Edg`, `Poly`, `Mesh`.
  * basic symmetry objects: `SpGrp` (space group), `Zell` (Zelling's symbol), `Sort` (sort of lattice).
  * information about all of 230 space groups (generators, centering type, symbol name).
  * information about dot-type Wyckoff positions and their stabilizers.
  * building of Voronoi cell with help of QHull lib.
  * building & filling unit cell from space group, basis and unit cell information.
  * detection of sort of lattice cell (from possible 24 Delaunay sorts).
  * minimization/normalization of reper, unit cell basis and Zelling's symbol.
  * OpenGL easy way visualisation of reper, unit cells, voronoi polyhedra and other stuff.
  * export to Ipe (vector editor) file format.
  * ready to use importer from ICSD database file format.


Where is examples / docs ?
==========================
In progress... You can find some usage examples in `./tmp` directory (some of them may be broken).
