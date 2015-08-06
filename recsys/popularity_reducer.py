#!/usr/bin/python

import sys

oldKey = None
count = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 1:
		continue

	thisKey = data[0]

	if oldKey and thisKey != oldKey:
		print "{0}\t{1}".format(oldKey, count)

		oldKey = thisKey
		count = 0

	oldKey = thisKey
	count += 1

if oldKey != None:
	print "{0}\t{1}".format(oldKey, count)

