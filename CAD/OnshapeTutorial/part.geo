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
//Mesh.VolumeFaces = 0;
Mesh.LabelType = 1;
Mesh.SurfaceNumbers = 1;
Mesh 3;
Save "gmsh.inp";
