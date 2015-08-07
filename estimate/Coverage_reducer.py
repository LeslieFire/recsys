#!/usr/bin/python
import sys

oldKey = None
trainSet = set()
recSet = set()

topN = 10
recDict = {}

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 2:
		thisKey, thisItem = data
	elif len(data) == 3:
		thisKey, thisItem, thisValue = data
	else:
		continue

	if oldKey and oldKey != thisKey:

		topItems = sorted(recDict, key=lambda x: recDict[x], reverse=True)[:topN]
		for item in topItems:
			recSet.add(item)

		oldKey = thisKey
		recDict.clear()

	oldKey = thisKey
	if len(data) == 2:
		trainSet.add(thisItem)
	if len(data) == 3:
		recDict[thisItem] = thisValue

if oldKey:
	topItems = sorted(recDict, key=lambda x: recDict[x], reverse=True)[:topN]
	for item in topItems:
		recSet.add(item)

print float("%.5f"% (len(recSet) / (len(trainSet) * 1.0)))






