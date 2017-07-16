#!/usr/bin/python
import sys

x = "pornhun.com"
#y = x + ".".rstrip('\n')
z = "." + x 
#l = x + "-".rstrip('\n')
k = "-" + x
print x
with open('namelist', 'r') as infile:
    for word in infile:
	neword = word.rstrip('\n')
        #h = y + word
        #print h.rstrip('\n')
        print neword + z
	#print l + neword
	print neword + k
