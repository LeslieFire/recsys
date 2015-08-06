#!/usr/bin/python

import sys

def Precision(train, test, N):
	hit = 0
	All = 0
	for user in train.keys():
		testItems = test[user]
		rank = GetRecommendation(user, N)
		for item, pui in rank:
			if item in testItems:
				hit += 1
		All += N

	return hit / (All * 1.0)