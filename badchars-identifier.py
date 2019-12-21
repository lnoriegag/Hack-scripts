#!/usr/bin/python
# -*- coding: utf-8 -*-
# Autor: @nogagmx

import argparse
from textwrap import wrap

parser = argparse.ArgumentParser()

parser.add_argument('-f','--file', dest='filename', required=True, 
	help="add file with chars admitted by the vulnerable software")
args = parser.parse_args()

filename = args.filename
# Create hexlist values
hexlist = [hex(i) for i in range(256)]

# Differences btw char lists
def Diff(badchars, chars): 
    dff = [i for i in badchars + chars if i not in badchars or i not in chars] 
    return dff 

goodchars = []
tmp = 0
f = open(filename, 'r+')
for line in f.readlines():
	l = line.split("  ")[1].rsplit()
	if len(l[0]) == 8:
		wrapped = wrap(l[0],2)
		for i in reversed(range (0,4)):
			if tmp != hex(255):
				goodchars.append(hex(int(wrapped[i],16)))
				tmp = goodchars[len(goodchars)-1]
 

print "[+] Badchars found: "+', '.join(Diff(goodchars,hexlist))


	
