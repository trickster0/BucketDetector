#!/usr/bin/python
domain=raw_input("domain/keyword: ")
with open("list.txt") as lines:
	for line in lines:
		print domain+"."+line.strip('\n')
		print line.rstrip()+"."+domain.strip('\n')
		print domain+"-"+line.strip('\n')
		print line.rstrip()+"-"+domain.strip('\n')
