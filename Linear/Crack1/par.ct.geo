// param.py par.ct.geo
// <B=20.>
// <a=20.5>
// <t=2.>
// CT specimen
B=<B>;   // Width
a=<a>;   // Crack length
t=<t>;   // Cut half width
// derived parameters
W=2*B;
s=0.55*W;
H=1.2*W;
D=0.25*W;
G=1.25*W;
// perimeter points
Point(1)={0,0,0,5};
Point(2)={W-a,0,0,0.1};
Point(3)={0.6*G,0,0,5};
Point(4)={0.6*G+t,t,0};
Point(5)={G,t,0};
Point(6)={G,H/2,0};
Point(7)={0,H/2,0};
// hole points
Point(8)={W,s/2,0};
Point(9)={W+D/2,s/2,0};
Point(10)={W,s/2+D/2,0};
Point(11)={W-D/2,s/2,0};
Point(12)={W,s/2-D/2,0};
//perimeter lines
Line(1)={1,2};
Line(2)={2,3};
Line(3)={3,4};
Line(4)={4,5};
Line(5)={5,6};
Line(6)={6,7};
Line(7)={7,1};
//hole
Circle(8)={9,8,10};
Circle(9)={10,8,11};
Circle(10)={11,8,12};
Circle(11)={12,8,9};
//Surface
Line Loop(12) = {1, 2,
  3, 4, 5, 6, 7};
Line Loop(13) = {8,9,10,11};
Plane Surface(14) = {12, 13};
//Solid
Extrude {0, 0, B/2} {Surface{14};}
//Meshing
Mesh.CharacteristicLengthMax = 10; // Maximum mesh element size
Mesh.ElementOrder=2;
Mesh.Optimize=1;
// Display control
Mesh.SurfaceEdges = 1;
Mesh.SurfaceFaces = 1;
Mesh 3;
// physical groups
Physical Surface("Symy")={30};
Physical Surface("Symz")={14};
Physical Surface("Load")={66,70};
Physical Volume("Part")={1};
Mesh.SaveGroupsOfNodes = 1;
General.Axes = 1;
Save "gmsh.inp";
Save "Refs/gmsh.png";
