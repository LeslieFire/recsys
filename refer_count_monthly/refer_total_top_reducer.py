#!/usr/bin/python

import sys

referCount = {}

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue

	thisKey, thisValue = data

	referCount[thisKey] = referCount.get(thisKey, 0) + int(thisValue)


topToLow = sorted(referCount, key=lambda x: referCount[x], reverse=True)
for key in topToLow:
	print "{0}\t{1}".format(key, referCount[key])