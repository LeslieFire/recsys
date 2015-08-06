#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import csv
import re
from datetime import datetime

# output : time \t ip \t request_page \t refer

# column 
# "ip"0, "-"1, "-"2, "Time"3, "DST"4, "request"5, "status"6 "body_bytes_sent"7 "http_referer"8
# "http_user_agent"9 "http_x_forwarded_for"10

# status == 200
# datetime.strptime(line[3][1:], "%d/%b/%Y:%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
# invalid request postfix .css , .js , .jpg, .jpeg, .png, .gif, .ico, .txt .swf .JPG  .PNG .xml static 
# valid refer postfix  .cn .com .gov .cc .info .org .net .travel
reader = csv.reader(sys.stdin, delimiter=" ")

for line in reader:
	if len(line) != 11:
		continue

	ip = line[0]
	time = datetime.strptime(line[3][1:], "%d/%b/%Y:%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
	request = line[5].strip().split()
	if len(request) != 3:
		continue
	refer = line[8]
	status = line[6]

	# filter unsuccess request
	if status != "200":
		continue

	# 去掉所有非页面访问
	if re.search(r"(\.js|\.css|\.gif|\.jpe?g|\.png|\.ico|\.txt | \.swf|\.JPE?G|\.PNG|\.xml|static)", request[1]):
		continue

	# 提取来源 url
	m = re.search(r"^https?://([^/]*\.(com|cn|gov|net|org|info|cc|travel)[^\?]*).*", refer)
	if m:
		print "{0}\t{1}\t{2}\t{3}".format(time, ip, request[1], m.group(1))
	elif refer == "-":
		print "{0}\t{1}\t{2}\t{3}".format(time, ip, request[1], refer)





