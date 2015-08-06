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

	ip = line[0]
	items = line[1].translate(None,delset).split()

	print "{0}\t{1}".format(ip, len(items))