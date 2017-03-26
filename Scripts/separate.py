#!/usr/bin/python
"""
This script replicates nodes to avoid nodal averaging of results.
The elements are scanned and if a node is used repeatedly, it is replaced by 
a new node at the same location and appropriate equations are generated.
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
    
# number of nodes and dofs per node
elprop={
    "B31":(2,6),
    "B31R":(2,6),
    "B32":(3,6),
    "B32R":(3,6),
    "C3D6":(6,3),
    "C3D4":(4,3),
    "C3D6":(6,3),
    "C3D8":(8,3),
    "C3D8I":(8,3),
    "C3D8R":(8,3),
    "C3D10":(10,3),
    "C3D15":(15,3),
    "C3D20":(20,3),
    "C3D20R":(20,3),
    "CAX3":(3,2),
    "CAX4":(4,2),
    "CAX4R":(4,2),
    "CAX6":(6,2),
    "CAX8":(8,2),
    "CAX8R":(8,2),
    "CPE3":(3,2),
    "CPE4":(4,2),
    "CPE4R":(4,2),
    "CPE6":(6,2),
    "CPE8":(8,2),
    "CPE8R":(8,2),
    "CPS3":(3,2),
    "CPS4":(4,2),
    "CPS4R":(4,2),
    "CPS6":(6,2),
    "CPS8":(8,2),
    "CPS8R":(8,2),
    "M3":(3,3),
    "M4":(4,3),
    "M4R":(4,3),
    "M6":(6,3),
    "M8":(8,3),
    "M8R":(8,3),
    "S3":(3,6),
    "S4":(4,6),
    "S4R":(4,6),
    "S6":(6,6),
    "S8":(8,6),
    "S8R":(8,6)
}
# initializing
datatype="unknown"
newelem=1
maxnode=1
usednodes=[]
nodes={}
elems=[]
f = open(source,"r")
fnodes = open("separate-nod.inc","w")
felems = open("separate-ele.inc","w")
feqn = open("separate-eqn.inc","w")
feqn.write("*EQUATION\n")

# read node table and element table
for line in f:
    if line.startswith("*"):
        # remove spaces and make uppercase
        line=(line.upper()).replace(" ","")
        if line.startswith("*NODE"):
            datatype="node"
            fnodes.write(line)
        elif line.startswith("*ELEMENT"):
            datatype="element"
            eltyp=line.split("TYPE=")[1].split(",")[0]
            numnodes=elprop[eltyp][0]
            numdofs=elprop[eltyp][1]
            felems.write(line)
            print eltyp, numnodes, numdofs
        else:
            datatype="unknown"
        continue
    if datatype=="node":
        # store the co-ordinates and update maxnode
        entries=line.split(",",1)
        number=int(entries[0])
        nodes[number]=entries[1]
        maxnode=max(maxnode,number)
        fnodes.write(line)
    if datatype=="element":
        # element entries can be multi-line
        if newelem:
            # reset the node list
            elist=[]
            numread=0
        # append data, remove eventual trailing comma
        line=line.replace(",\n","")
        elist.append([int(field) for field in line.split(",")])
        numread+=len(elist[-1])
        # check if data is complete
        if numread-1==numnodes:
            newelem=1
            # now process the element
            # write element number and remove it from elist
            felems.write("{0},".format(elist[0][0]))
            elist[0]=elist[0][1:]
            # iterate over nodes of the element
            for dataline in elist:
                for number in dataline:
                    if not (number in usednodes):
                        # write number as is and register usage
                        felems.write("{0},".format(number))
                        usednodes.append(number)
                    else:
                        # create a new node and use this instead
                        maxnode+=1
                        fnodes.write("{0},".format(maxnode)+nodes[number])
                        felems.write("{0},".format(maxnode))
                        # create the equations to couple the nodes
                        for i in range(numdofs):
                            feqn.write("2\n")
                            feqn.write("{0},{1},1,{2},{1},-1\n".format(maxnode,i+1,number))
                felems.write("\n")
        else:
            newelem=0
f.close()
fnodes.close()
felems.close()
feqn.close()


