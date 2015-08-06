#!/usr/bin/python
import sys
import csv
import string

reader = csv.reader(sys.stdin, delimiter="\t")
next(reader, None)
delset = string.punctuation
for line in reader:
	if len(line) != 2:
		continue

	items = line[1].translate(None,delset).split()

	for item in items:
		print "{0}".format(item)