#!/usr/bin/python

import sys

oldIp = None
route = []

print "IP\tROUTE_ID"

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	thisIp, thisRouteId = data

	if oldIp and oldIp != thisIp:
		print "{0}\t{1}".format(oldIp, route)

		oldIp = thisIp
		del route[:]

	oldIp = thisIp
	if thisRouteId not in route:
		route.append(thisRouteId)

if oldIp != None:
	print "{0}\t{1}".format(oldIp, route)