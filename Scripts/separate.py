#!/usr/bin/python
"""
This script replicates nodes to avoid nodal averaging of results.
The elements are scanned and if a node is used repeatedly, it is replaced by
a new node at the same location and appropriate equations are generated.
"""
import sys

# processing command line arguments, get the
# jobname
if len(sys.argv)>1:
    print "Using file:",sys.argv[1]
    source = sys.argv[1]
else:
    print "Specify mesh file"
    quit()

# 0 number of nodes
# 1 dofs per node
# 2 cgx name (elty)
# 3 cgx type number
# 4 cgx attribute
elprop={
    "B31"   :( 2,6,"be2",   11,  0),
    "B31R"  :( 2,6,"",      11,  1),
    "B32"   :( 3,6,"",      12,  0),
    "B32R"  :( 3,6,"",      12,  1),
    "C3D4"  :( 4,3,"te4",    3,  0),
    "C3D6"  :( 6,3,"pe6",    2,  0),
    "C3D8"  :( 8,3,"he8",    1,  0),
    "C3D8I" :( 8,3,"he8i",   1,  2),
    "C3D8R" :( 8,3,"he8r",   1,  1),
    "C3D10" :(10,3,"te10",   6,  0),
    "C3D15" :(15,3,"pe15",   5,  0),
    "C3D20" :(20,3,"he20",   4,  0),
    "C3D20R":(20,3,"he20r",  4,  1),
    "CAX3"  :( 3,2,"tr3c",   7,  6),
    "CAX4"  :( 4,2,"qu4c",   9,  6),
    "CAX4R" :( 4,2,"qu4cr",  9, 16),
    "CAX6"  :( 6,2,"tr6c",   8,  6),
    "CAX8"  :( 8,2,"qu8",   10,  6),
    "CAX8R" :( 8,2,"qu8r",  10, 16),
    "CPE3"  :( 3,2,"tr3e",   7,  4),
    "CPE4"  :( 4,2,"qu4e",   9,  4),
    "CPE4R" :( 4,2,"qu4er",  9, 14),
    "CPE6"  :( 6,2,"tr6e",   8,  4),
    "CPE8"  :( 8,2,"qu8e",  10,  4),
    "CPE8R" :( 8,2,"qu8er", 10, 14),
    "CPS3"  :( 3,2,"tr3s",   7,  5),
    "CPS4"  :( 4,2,"qu4s",   9,  5),
    "CPS4R" :( 4,2,"qu4sr",  9, 15),
    "CPS6"  :( 6,2,"tr6s",   8,  5),
    "CPS8"  :( 8,2,"qu8s",  10,  5),
    "CPS8R" :( 8,2,"qu8sr", 10, 15),
    "M3"    :( 3,3,"",       7, ""),
    "M4"    :( 4,3,"",       9, ""),
    "M4R"   :( 4,3,"",       9, ""),
    "M6"    :( 6,3,"",       8, ""),
    "M8"    :( 8,3,"",      10, ""),
    "M8R"   :( 8,3,"",      10, ""),
    "S3"    :( 3,6,"tr3",    7,  0),
    "S4"    :( 4,6,"qu4",    9,  0),
    "S4R"   :( 4,6,"qu4r",   9,  1),
    "S6"    :( 6,6,"tr6",    8,  0),
    "S8"    :( 8,6,"qu8",   10,  0),
    "S8R"   :( 8,6,"qu8r",  10,  1)
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
