#!/usr/bin/python
import os

FOLDERPATH = "css/"


# Get list of all files in the folder


# Open up each file one by one
dirlist=os.listdir(FOLDERPATH)

try:
    masterfile = open('stylesheet.css', 'w')
    for fname in dirlist:
        try:
            thefile = open(FOLDERPATH+fname, 'r')
            print fname + " opened."
        
            for line in thefile.readlines():
                if(line.startswith('  background:') or line.startswith('  background-image:')):
                    line = line.replace("../images/", "%%")
                    line = line.replace(".png')", "%%')")

                    ##] Get rid more more annoying dev stuff
                    line = line.replace("sprites/", "")
                    line = line.replace("icons/", "")
                    masterfile.write(line)
                else:         
                    masterfile.write(line)

            thefile.close()
        except IOError as e:
            print "Couldn't open file " + e

except IOError as e:
    print "Couldn't open file " + e