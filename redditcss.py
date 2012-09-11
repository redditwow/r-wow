#!/usr/bin/python
# The most ghetto script you will probably ever find.
# Reads a bunch of css files and replaces local image refs to
# refs that will work on reddit. Requires code to be indented with
# two spaces and the line must start with certain properties. I
# really didn't want to bother with regex. Too annoying for this.
# Written by Robert "Fluxflashor" Veitch
import os

FOLDERPATH = "css/"

# Open up each file one by one
dirlist=os.listdir(FOLDERPATH)

try:
    masterfile = open('stylesheet.css', 'w')
    for fname in dirlist:
        try:
            thefile = open(FOLDERPATH+fname, 'r')
            print fname + " opened"
        
            for line in thefile.readlines():
                if line.startswith('  background:') or line.startswith('  background-image:') or line.startswith('  content:'):
                    print "--\nMatched ("+fname+"):\nOld Line: " + line

                    line = line.replace("../images/", "%%")
                    line = line.replace(".png')", "%%')")
                    line - line.replace(".jpg')", "%%')")

                    ##] Get rid more more annoying dev stuff
                    line = line.replace("sprites/", "")
                    line = line.replace("icons/", "")
                    line = line.replace("_", "-")
                    print "New Line: " + line

                    masterfile.write(line)
                else:         
                    masterfile.write(line)

            thefile.close()
            print fname + " closed."
        except IOError as e:
            print "Couldn't open file " + e

except IOError as e:
    print "Couldn't open file " + e