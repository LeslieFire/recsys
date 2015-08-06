#!/usr/bin/python

# see what kind of file contains   static

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter="\t")

for line in reader:
	if len(line) != 4:
		continue

	time, ip, request, refer = line

	if re.search(r"static", request):
		m = re.search(r"^([^/]*\.(com|cn|gov|net|org|info|cc|travel)[^\?]*).*", refer)
		if m:
			print "{0}\t{1}\t{2}\t{3}".format(time, ip, request, m.group(1))
		elif refer == "-":
			print "{0}\t{1}\t{2}\t{3}".format(time, ip, request, refer)