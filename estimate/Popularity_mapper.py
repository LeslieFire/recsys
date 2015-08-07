#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		continue

	userId, item = data
	print "{0}\t{1}".format(item, 1)