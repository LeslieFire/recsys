#!/usr/bin/python
import sys
import re
import csv

# column 
# "ip"0, "-"1, "-"2, "Time"3, "DST"4, "request"5, "status"6 "body_bytes_sent"7 "http_referer"8
# "http_user_agent"9 "http_x_forwarded_for"10
# date format %d/%b/%Y:%H:%M:%S
# datetime.strptime(line[3][1:12], "%d/%b/%Y:%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
# datetime.strptime(line[3][1:12], "%d/%b/%Y").strftime("%Y-%m-%d")
# weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
# [29/Jul/2015:16:09:44
reader = csv.reader(sys.stdin, delimiter=" ")

for line in reader:
	if len(line) != 11:
		continue

	if len(line[3]) < 21:
		continue

	ip = line[0]
	status = line[6]
	request = line[5].strip().split()
	if len(request) != 3:
		continue

	m = re.search(r"^/route/routeId(\d+).html", request[1])
	if m and status == "200":
		print "{0}\t{1}".format(ip, m.group(1))