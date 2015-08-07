#/usr/bin/python

# input < item, popularity > or < userID, recommend list>
# output < item, 'A', popularity > or < recommendItem, 'B'>

import sys

topN = 3 # 5, 10

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue

	itemOrID, popuOrRecList = data

	if popuOrRecList[0] == '[':
		items = [ item for item in popuOrRecList[1:-1].strip().split(",")]
		for i in range(topN):
			if i >= len(items):
				break
			item, pui = items[i].strip().split(":")
			print "{0}\t{1}".format(item, 'B')
	else:
		print "{0}\t{1}\t{2}".format(itemOrID, 'A', popuOrRecList)