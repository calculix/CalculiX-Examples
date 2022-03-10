d = 10; // Nenndurchmesser
s = 17; // Schluesselweite
k = 7; // Kopfhoehe
m = 0.8*d; // Mutternhoehe

db = 11; //Bohrungsdurchmesser
t1 = 10; //Plattendicke 1
b1 = 40;
l1 = 40;
t2 = 15; //Plattendicke 2
b2 = 50;
l2 = 45;

t3 = 10; //Stegdicke
h3 = 30; //Steghoehe
e = 20; //halber Schraubenabstand

Point(1) = {e,0,-t2}; // Mittelpunkt der Schraube
Point(2) = {e,0,t1+k};
Point(3) = {e,s/2,t1+k};
Point(4) = {e,s/2,t1};
Point(5) = {e,d/2,t1};
Point(6) = {e,d/2,-t2};
Point(7) = {e,0,-t2-m};
Point(8) = {e,s/2,-t2-m};
Point(9) = {e,s/2,-t2};
Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,5};
Line(5) = {5,6};
Line(6) = {6,1};
Line Loop(1) = {1,2,3,4,5,6};
Plane Surface(1) ={1};
Line(7) = {1,7};
Line(8) = {7,8};
Line(9) = {8,9};
Line(10) = {9,6};
Line Loop(2) = {7,8,9,10,6};
Plane Surface(2) ={2};

pc=newp;
Point(pc) = {0,0,0};
out[] = Extrude { {0,0,1}, {e,0,0}, Pi/2 } { Surface{1,2}; };
out[] = Symmetry {0,1,0,0}  { Duplicata{ Volume{1,2}; } };
out[] = Symmetry {-1,0,0,20}  { Duplicata{ Volume{1,2,98,60}; } };

//Reverse Surface {84,145,181,120};

Physical Surface("C_head") = {-84, 29, 245, -145};
Physical Surface("C_nut") = {55, -120, -181, 212};

// Platten
// Platte 1
// Aussenrand
pp1 = newp;
Point(pp1) = {0,b1/2,0};
Point(pp1+1) = {l1,b1/2,0};
Point(pp1+2) = {l1,-b1/2,0};
Point(pp1+3) = {0,-b1/2,0};
ll1 = newl;
Line(ll1) = {pp1,pp1+1};
Line(ll1+1) = {pp1+1,pp1+2};
Line(ll1+2) = {pp1+2,pp1+3};
Line(ll1+3) = {pp1+3,pp1};
ll = newll;
Line Loop(ll) = {ll1,ll1+1,ll1+2,ll1+3};
// Bohrung
pp1 = newp;
Point(pp1) = {e,0,0};
Point(pp1+1) = {e,db/2,0};
Point(pp1+2) = {e+db/2,0,0};
Point(pp1+3) = {e,-db/2,0};
Point(pp1+4) = {e-db/2,0,0};
ll1 = newl;
Circle(ll1) = {pp1+1,pp1,pp1+2};
Circle(ll1+1) = {pp1+2,pp1,pp1+3};
Circle(ll1+2) = {pp1+3,pp1,pp1+4};
Circle(ll1+3) = {pp1+4,pp1,pp1+1};
Line Loop(ll+1) = {ll1,ll1+1,ll1+2,ll1+3};
ns = news;
Plane Surface(ns) ={ll,ll+1};
Out[] = Extrude {0,0,t1} { Surface{ns}; };

// Platte 2
// Aussenrand
eps = -0.001;
pp1 = newp;
Point(pp1) = {0,b2/2,eps};
Point(pp1+1) = {l2,b2/2,eps};
Point(pp1+2) = {l2,-b2/2,eps};
Point(pp1+3) = {0,-b2/2,eps};
ll1 = newl;
Line(ll1) = {pp1,pp1+1};
Line(ll1+1) = {pp1+1,pp1+2};
Line(ll1+2) = {pp1+2,pp1+3};
Line(ll1+3) = {pp1+3,pp1};
ll = newll;
Line Loop(ll) = {ll1,ll1+1,ll1+2,ll1+3};
// Bohrung
pp1 = newp;
Point(pp1) = {e,0,eps};
Point(pp1+1) = {e,db/2,eps};
Point(pp1+2) = {e+db/2,0,eps};
Point(pp1+3) = {e,-db/2,eps};
Point(pp1+4) = {e-db/2,0,eps};
ll1 = newl;
Circle(ll1) = {pp1+1,pp1,pp1+2};
Circle(ll1+1) = {pp1+2,pp1,pp1+3};
Circle(ll1+2) = {pp1+3,pp1,pp1+4};
Circle(ll1+3) = {pp1+4,pp1,pp1+1};
Line Loop(ll+1) = {ll1,ll1+1,ll1+2,ll1+3};
ns = news;
Plane Surface(ns) = {ll,ll+1};
Out[] = Extrude {0,0,-t2} { Surface{ns}; };

Physical Surface("sym1") = {285};
Physical Surface("sym2") = {337};
Physical Surface("c1o") = {302};
Physical Surface("c1u") = {260};
Physical Surface("c2o") = {312};
Physical Surface("c2u") = {354};
Physical Surface("c2r") = {329};
Physical Volume("bolt") = {1,2,60,121,221,98,159,190};
Physical Volume("p1") = {222};
Physical Volume("p2") = {223};

Mesh.ElementOrder = 2;
Mesh 3;
	
Mesh.SaveGroupsOfNodes = 1;

Save "Bolt-gmsh.inp";