Merge "part.step";

// Virtual topology to avoid enforcing small elements
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
Mesh.CharacteristicLengthMax = 7;
//Mesh.CharacteristicLengthFromCurvature = 1;
//Mesh.MinimumCirclePoints = 36;
//Transfinite Curve {61,68} = 10;
//Transfinite Curve {28,70} = 20;
//Transfinite Curve {52,58} = 10;
Mesh.CompoundCharacteristicLengthFactor = 0.3;
Mesh.CompoundClassify = 0;
Mesh.HighOrderOptimize = 1;
Mesh.ElementOrder = 2;

Mesh 3;
Mesh.SaveGroupsOfNodes = 1;
Save "gmshVT.inp";
// image
Mesh.SurfaceEdges = 0;
Mesh.SurfaceFaces = 0;
Mesh.VolumeEdges = 1;
Mesh.VolumeFaces = 1;
General.Trackball=0;
General.RotationX=-50;
// Geometry.HideCompounds = 1;

Save "Refs/gmshVT.png";
General.RotationX=-260;
General.RotationY=23;
General.ScaleX = 2.5;
General.ScaleY = 2.5;
General.ScaleZ = 2.5;
General.TranslationX = -40; // X-axis translation (in model units)
General.TranslationY = 10; // Y-axis translation (in model units)
Save "Refs/gmshVT-zoom.png";
