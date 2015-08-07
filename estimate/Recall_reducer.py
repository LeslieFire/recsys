#/usr/bin/python

# input 
# < userID, testItem > or < userID, recItem, score >
# output : recall ratio

import sys

oldKey = None
testSet = set()
recDict = {}

hit = 0
testAll = 0
topN = 3

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 2:
		thisKey, thisItem = data
	elif len(data) == 3:
		thisKey, thisItem, thisValue = data
	else:
		continue

	if oldKey and thisKey != oldKey:
		topItems = sorted(recDict, key=lambda x: recDict[x], reverse=True)[:topN]
		for item in topItems:
			if item in testSet:
				hit += 1
		recDict.clear()
		testAll += len(testSet)
		testSet.clear()

	oldKey = thisKey
	if len(data) == 2:
		testSet.add(thisItem)
	else:
		recDict[thisItem] = thisValue

if oldKey:
	topItems = sorted(recDict, key=lambda x: recDict[x], reverse=True)[:topN]
	for item in topItems:
		if item in testSet:
			hit += 1
	recDict.clear()
	testAll += len(testSet)
	testSet.clear()

print float("%.5f"% (hit / (testAll * 1.0)))





