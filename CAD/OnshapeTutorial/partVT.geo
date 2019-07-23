Merge "part.step";
// Virtual topology to avoid enforcing small elements
/*Compound Line(1000)={63,64};
Compound Line(1001)={65,66};
Compound Surface(30) = {23,25};
Compound Surface(31) = {9,24,26};
Compound Surface(32) = {21};
Compound Surface(33) = {22};*/
Compound Curve {63,64};
Compound Curve {65,66};
Compound Surface {23,25};
Compound Surface {9,24,26};
Compound Surface {21};
Compound Surface {22};
// Set definitions
Physical Surface("support") = {5};
Physical Surface("load") = {17};
Physical Volume("part") = {1};
// Mesh control and meshing
Mesh.SaveGroupsOfNodes = 1;
Mesh.CharacteristicLengthMax = 5;
Mesh.ElementOrder=2;
Mesh.Optimize=1;
Mesh.CompoundClassify=0;
// Mesh.RemeshParametrization = 7;
Mesh 3;
Save "gmshVT.inp";
// image
// in script mode, there is bad image quality
Mesh.SurfaceEdges = 0;
Mesh.SurfaceFaces = 0;
Mesh.VolumeEdges = 1;
Mesh.VolumeFaces = 1;
General.Trackball=0;
General.RotationX=-50;
// Geometry.HideCompounds = 1;

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
