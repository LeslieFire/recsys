#!/usr/bin/python

import sys

# input 
# test data : userID 	itemID
# recommend data : userID 	recommendList

# output 
# < userID, testItem > or < userID, recItem, score >

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	userId, itemOrList = data
	if itemOrList[0] == '[':
		items = [ item for item in itemOrList[1:-1].strip().split(",")]
		for ip in items:
			item, pui = ip.strip().split(":")
			print "{0}\t{1}\t{2}".format(userId, item, pui)
	else:
		print "{0}\t{1}".format(userId, itemOrList)


