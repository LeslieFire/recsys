#!/usr/bin/python
import sys

oldKey = None
monthCount = {}

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue

	thisKey, thisMonth = data

	if oldKey and oldKey != thisKey:
		sortedKeys = sorted(monthCount)
		for key in sortedKeys:
			print "{0}\t{1}\t{2}".format(oldKey, key, monthCount[key])
		oldKey = thisKey
		monthCount.clear()


	oldKey = thisKey
	monthCount[thisMonth] = monthCount.get(thisMonth, 0) + 1

if oldKey != None:
	sortedKeys = sorted(monthCount)
	for key in sortedKeys:
		print "{0}\t{1}\t{2}".format(oldKey, key, monthCount[key])
