#!/usr/bin/python

import sys

referCount = {}
monthCount = {}
referMonthCount = {}

oldKey = None
count = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 3:
		continue

	thisKey, thisMonth, thisValue = data
	if oldKey and oldKey != thisKey:
		# save
		referCount[oldKey] = count
		referMonthCount[oldKey] = monthCount

		# clear
		count = 0
		oldKey = thisKey
		monthCount = {}

	oldKey = thisKey
	count += int(thisValue)
	monthCount[thisMonth] = monthCount.get(thisMonth, 0) + int(thisValue)

	
if oldKey:
	referCount[oldKey] = count
	referMonthCount[oldKey] = monthCount

topToLow = sorted(referCount, key=lambda x: referCount[x], reverse=True)
for key in topToLow:
	month = referMonthCount[key]
	sortedMonthCount = sorted(month)
	for m in sortedMonthCount:
		print "{0}\t{1}\t{2}".format(key, m, month[m])




