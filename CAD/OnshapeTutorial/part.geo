// Geometry.Tolerance=0.1;
//Geometry.OCCFixSmallEdges=1;
//Geometry.OCCFixSmallFaces=1;
Merge "part.step";
// Mesh control
Mesh.ElementOrder=2;
Mesh.Optimize=1;
// Display control
//Mesh.SurfaceEdges = 1;
Mesh.SurfaceFaces = 1;
Mesh.VolumeEdges = 0;
Mesh.HighOrderOptimize = 2;
//Mesh.CharacteristicLengthMax = 10;
//Mesh.VolumeFaces = 0;
Mesh 3;
Physical Surface("support") = {5};
Physical Surface("load") = {17};
Physical Volume("part") = {1};
Mesh.SaveGroupsOfNodes = 1;
Save "gmsh.inp";
