#!/usr/bin/python
import sys


print "TIME\tIP\tREQUEST\tSOURCE"
for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 4:
		continue
		
	print "{0}\t{1}\t{2}\t{3}".format(data[0], data[1], data[2], data[3])
