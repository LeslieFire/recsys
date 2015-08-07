#/usr/bin/python

import sys
import math


# input : < item, 'A', popularity > or < recommendItem, 'B'>
# output : average popularity  and  max popularity

oldKey = None

count = 0
totalCount = 0
totalPopu = 0
popularity = 0

maxPopularity = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 2:
		thisKey, thisType = data
	elif len(data) == 3:
		thisKey, thisType, thisPopu = data
	else:
		continue

	if oldKey and oldKey != thisKey:

		totalPopu += count * math.log(1 + popularity)
		totalCount += count

		oldKey = thisKey
		count = 0
		popularity = 0

	oldKey = thisKey
	if thisType == 'A':
		popularity = int(thisPopu)
		if popularity > maxPopularity:
			maxPopularity = popularity
	elif thisType == 'B':
		count += 1

if oldKey:
	totalPopu += count * math.log(1 + popularity)
	totalCount += count

print float("%.5f"%(totalPopu /(totalCount * 1.0))), " max popularity : ", math.log(1 + maxPopularity)
