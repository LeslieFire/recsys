#/usr/bin/python


# input : itemID 1
# output : itemID popularity

import sys

oldKey = None
count = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue

	thisKey, thisCount = data

	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, count)

		count = 0
		oldKey = thisKey

	oldKey = thisKey
	count += int(thisCount)

if oldKey:
	print "{0}\t{1}".format(oldKey, count)