#!/usr/bin/python

# function: merge the same source; ie. www.baidu.com , image.baidu.com -> baidu.com
# input : refer count
# output: refer count

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter = "\t")

replaceDict = {
	"baidu.": 	"baidu.com",
	"sogou.": 	"sogou.com",
	"weixin.": 	"weixin.qq.com",
	"36kr.": 	"36kr.com",
	"lagou.":	"lagou.com",
	"58.":		"58.com",
	"17ce.": 	"17ce.com",
	"sm.":		"sm.cn",
	"so.":		"haosou.com",
	"haosou.":	"haosou.com",
	"koudaitong.":"koudaitong.com",
	"traveldaily.":"traveldaily.cn",
	"zhaopin.":	"zhaopin.com",
	"zhiyoula.":"zhiyoula.com",
	"gogogous.":	"gogogous.com",
	"weibo.":"weibo.com",
	"cnzz.": "cnzz.com",
	"51job.":	"51job.com",
	"ganji.":	"ganji.com",
	"itatour.":	"itatour.net",
	"ctcnn.":	"ctcnn.com",
	"chuangyepu.":"chuangyepu.com",
	"coinvest.":"chuangyepu.com",
	"jfenz.": "jfenz.com",
	"bing.":		"bing.com",
	"360.":		"360.com",
	"jobui.":	"jobui.com",
	"zhubajie.": "zhubajie.com",
	"google.":	"google.com",
	"pinchain.":	"pinchain.com",
	"hao123.":	"hao123.com",
	"facebook.":	"facebook.com",
	"dajie.":	"dajie.com"
}

for line in reader:
	if len(line) != 3:
		continue

	refer, month, count = line

	for key in replaceDict.keys():
		if re.search(key, refer):
			refer = replaceDict[key]
			break

	print "{0}\t{1}\t{2}".format(refer, month, count)



