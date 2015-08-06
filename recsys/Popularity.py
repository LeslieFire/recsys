#!/usr/bin/python
# -*- coding: uft-8 -*-
import sys

def Popularity(train, test, N):
	item_popularity = dict()
	for user, items in train.items():
		for item in items:
			if item not in item_popularity:
				item_popularity[item] = 0
			item_popularity[item] += 1

	N = 0
	p = 0
	for user in train.keys():
		rank = GetRecommendation(user, N)
		for item, pui in rank:
			p += math.log(1 + item_popularity[item])
			N += 1

	return p / ( N * 1.0 )

# 计算平均流行度时对每个物品的流行度取对数，
# 因为物品的流行度分布满足长尾分布，在取对数后，流行度的平均值更加稳定