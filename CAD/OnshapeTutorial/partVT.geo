Merge "part.step";
// Virtual topology to avoid enforcing small elements
Compound Line(1000)={63,64};
Compound Line(1001)={65,66};
Compound Surface(30) = {23,25};
Compound Surface(31) = {9,24,26};
Compound Surface(32) = {21};
Compound Surface(33) = {22};
// Set definitions
Physical Surface("support") = {5};
Physical Surface("load") = {17};
Physical Volume("part") = {1};
// Mesh control and meshing
Mesh.SaveGroupsOfNodes = 1;
Mesh.ElementOrder=2;
Mesh.Optimize=1;
Mesh 3;
Save "gmshVT.inp";
// image
// in script mode, there is bad image quality
Mesh.SurfaceEdges = 1;
Mesh.SurfaceFaces = 1;
Mesh.VolumeEdges = 0;
Mesh.VolumeFaces = 0;
General.Trackball=0;
General.RotationX=-50;
Geometry.HideCompounds = 1;

Save "gmshVT.png";
Save "gmshVT.gif";
Save "gmshVT.pdf";
General.RotationX=-260;
General.RotationY=23;
General.ScaleX = 2.5;
General.ScaleY = 2.5;
General.ScaleZ = 2.5;
General.TranslationX = -40; // X-axis translation (in model units)
General.TranslationY = 10; // Y-axis translation (in model units)
Save "gmshVT-zoom.png";
Save "gmshVT-zoom.gif";
Save "gmshVT-zoom.pdf";
