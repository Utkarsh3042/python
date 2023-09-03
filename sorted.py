import os
import sys

fname = input("Enter the file name whose content are to be sorted :")

if not os.path.isfile(fname):
    print(fname,'doesnt exist')
    sys.exit(0)

infile = open(fname,'r')
myList = infile.readlines()
print(myList)

linelist = []
for line in myList:
    linelist.append(line.strip())

linelist.sort()

outfile = open('sorted.txt','w')

for line in linelist:
    outfile.write(line+"\n")

infile.close()
outfile.close()

if os.path.isfile('sorted.txt'):
    print("\nFile containing sorted content sorted.txt created successfully")
    print("sorted.txt contains", len(linelist), "lines")
    print("Contents of sorted.txt")
    print("=================================================================")
    rdFile = open("sorted.txt","r")
    for line in rdFile:
        print(line, end="")
