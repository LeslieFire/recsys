#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import csv

delset = ".'[],"
for line in sys.stdin:
	if "IP" in line:
		continue
	line = line.translate(None, delset)

	print line.strip()
	
