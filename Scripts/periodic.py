#!/usr/bin/python
"""
This script creates equations for periodic boundary conditions of a brick-shaped RVE. We assume that it's corners are at (0,0,0) and (lx,ly,lz).
The dimensions are determined from the nodal co-ordinates.

"""
import sys
import numpy

# processing command line arguments, get the
# jobname
if len(sys.argv)>1:
    print "Using file:",sys.argv[1]
    source = sys.argv[1]
else:
    print "Specify mesh file"
    quit()
    
# initializing
datatype="unknown"
nodes=[]
f = open(source,"r")
fo = open("periodic.equ","w")

# read node table
for line in f:
    if line.startswith("*"):
        # remove spaces and make uppercase
        line=(line.upper()).replace(" ","")
        if line.startswith("*NODE"):
            datatype="node"
        else:
            datatype="unknown"
        continue
    if datatype=="node":
        # print [float(field) for field in line.split(",")]
        nodes.append([float(field) for field in line.split(",")])      
f.close()
na=numpy.array(nodes)
n=numpy.int_(na[:,0])
x=numpy.array(na[:,1])
y=numpy.array(na[:,2])
z=numpy.array(na[:,3])


# determine dimensions of the brick
[lx,ly,lz]=[x.max(),y.max(),z.max()]
print "lx: {0}\nly: {1}\nlz: {2}".format(lx,ly,lz)

# determine control nodes
x0=numpy.extract(x==0.,n)
y0=numpy.extract(y==0.,n)
z0=numpy.extract(z==0.,n)
xl=numpy.extract(x==lx,n)
yl=numpy.extract(y==ly,n)
zl=numpy.extract(z==lz,n)
n0=numpy.extract([pt==[0.,0.,0.] for pt in na[:,1:].tolist()],n)[0]
nx=numpy.extract([pt==[lx,0.,0.] for pt in na[:,1:].tolist()],n)[0]
ny=numpy.extract([pt==[0.,ly,0.] for pt in na[:,1:].tolist()],n)[0]
nz=numpy.extract([pt==[0.,0.,lz] for pt in na[:,1:].tolist()],n)[0]
print "n0: {0}\nnx: {1}\nny: {2}\nnz: {3}".format(n0,nx,ny,nz)

fo.write("**set definitions\n")
fo.write("*nset, nset=n0\n{0}\n".format(n0))
fo.write("*nset, nset=nx\n{0}\n".format(nx))
fo.write("*nset, nset=ny\n{0}\n".format(ny))
fo.write("*nset, nset=nz\n{0}\n".format(nz))

"""
Create the equations:
ux_j=ux_i+ux_nx on all inner points

"""
fo.write("*equation\n")
constrained=[n0,nx,ny,nz]
# eliminate nodes at xl
for i in x0:
    for j in xl:
        if (y[i-1]==y[j-1] and z[i-1]==z[j-1]):
            if j not in constrained:
                fo.write("3\n{0},1,-1,{1},1,1,{2},1,1\n".format(j,i,nx))
                fo.write("3\n{0},2,-1,{1},2,1,{2},2,1\n".format(j,i,nx))
                fo.write("3\n{0},3,-1,{1},3,1,{2},3,1\n".format(j,i,nx))
                constrained.append(j)
# eliminate nodes at yl
for i in y0:
    for j in yl:
        if (x[i-1]==x[j-1] and z[i-1]==z[j-1]):
            if j not in constrained:
                fo.write("3\n{0},1,-1,{1},1,1,{2},1,1\n".format(j,i,ny))
                fo.write("3\n{0},2,-1,{1},2,1,{2},2,1\n".format(j,i,ny))
                fo.write("3\n{0},3,-1,{1},3,1,{2},3,1\n".format(j,i,ny))
                constrained.append(j)
# find pairs x0-xl
for i in z0:
    for j in zl:
        if (y[i-1]==y[j-1] and x[i-1]==x[j-1]):
            if j not in constrained:
                fo.write("3\n{0},1,-1,{1},1,1,{2},1,1\n".format(j,i,nz))
                fo.write("3\n{0},2,-1,{1},2,1,{2},2,1\n".format(j,i,nz))
                fo.write("3\n{0},3,-1,{1},3,1,{2},3,1\n".format(j,i,nz))
                constrained.append(j)
print "{0} nodes constrained".format(len(constrained))
fo.close()
