#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter="\t")
next(reader, None)

for line in reader:
	if len(line) != 2:
		continue

	print "{0}\t{1}".format(line[0], line[1])
	break