#!/usr/bin/python
import sys
import csv
import re

# input: time  ip  request  refer
# output: refer month

# filter: get url by cut the string behind "/"

# replace dict
replaceDict = {
	"sinbad":"sinbad.com.cn",
	"www.baidu.com":"www.baidu.com"
}

reader = csv.reader(sys.stdin, delimiter="\t")
next(reader, None)

for line in reader:
	if len(line) != 4:
		continue

	month = line[0][:7]
	refer = line[3]

	for key in replaceDict.keys():
		if re.search(key, refer):
			refer = replaceDict[key]
			break

	m = re.search(r"^([^/]*)", refer)
	if m:
		print "{0}\t{1}".format(m.group(1), month)
	elif refer == "-":
		print "{0}\t{1}".format(refer, month)
