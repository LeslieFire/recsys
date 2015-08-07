#/usr/bin/python

import sys
import os

M = 8

# calculate coverage
totalCoverage = 0.0
aveCoverage = 0.0
for k in range(M):
	cmd = 'cat train_data'+ str(k) +' recsheet/recsheet'+ str(k) + '.txt | python Coverage_mapper.py |sort | python Coverage_reducer.py'
	tmp = os.popen(cmd).readline()
	totalCoverage += float(tmp.strip())
aveCoverage = totalCoverage / M;

print "Coverage : " , float("%.5f"% (aveCoverage))

# calculate precision
totalPrecision = 0.0
avePrecision = 0.0
for k in range(M):
	cmd = 'cat test_data'+ str(k) +' recsheet/recsheet'+ str(k) + '.txt | python Coverage_mapper.py |sort | python Precision_reducer.py'
	tmp = os.popen(cmd).readline()
	totalPrecision += float(tmp.strip())
avePrecision = totalPrecision / M;

print "Precision : " , float("%.5f"% (avePrecision))

# calculate recall
totalRecall = 0.0
aveRecall = 0.0
for k in range(M):
	cmd = 'cat test_data'+ str(k) +' recsheet/recsheet'+ str(k) + '.txt | python Coverage_mapper.py |sort | python Recall_reducer.py'
	tmp = os.popen(cmd).readline()
	totalRecall += float(tmp.strip())
aveRecall = totalRecall / M;

print "Recall : " , float("%.5f"% (aveRecall))

# calculate popularity
# for k in range(M):
# 	cmd = 'cat train_data'+ str(k) +' | python Popularity_mapper.py |sort |python Popularity_reducer.py > popularity'+ str(k) + '.txt'
# 	os.system(cmd)


# calculate liveness
# cat popularity0.txt recsheet/recsheet0.txt | python liveness_mapper.py |sort | python liveness_reducer.py
totalLiveness = 0.0
aveLiveness = 0.0
totalMaxLive = 0.0
aveMaxLive = 0.0
for k in range(M):
	cmd = 'cat popularity'+str(k)+'.txt recsheet/recsheet'+str(k)+'.txt | python liveness_mapper.py |sort | python liveness_reducer.py'
	tmp = os.popen(cmd).readline()
	liveness, maxliveness = tmp.strip().split("\t")
	
	totalLiveness += float(liveness)
	totalMaxLive += float(maxliveness)

aveLiveness = totalLiveness / (M * 1.0)
aveMaxLive = totalMaxLive / (M * 1.0)

print "liveness : ", float("%.5f"% (aveLiveness)), " maxliveness : ", float("%.5f"% (aveMaxLive))


