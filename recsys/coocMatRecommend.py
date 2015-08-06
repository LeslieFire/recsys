#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import operator
import csv
import string
import pprint
import random
import math

def splitData(data, k, M, seed):
	test = []
	train = []
	random.seed(seed)
	for user, item in data:
		if random.randint(0, M) == k:
			test.append([user, item])
		else:
			train.append([user, item])

	return train, test

def Recall(train, test, W, N):
	hit = 0
	All = 0
	for user in train.keys():
		if user not in test.keys():
			continue
		testItems = test[user]
		rank = GetRecommendation(train, user, W, N)
		for item, pui in rank.items():
			if item in testItems:
				hit += 1
		All += len(testItems)
	return float("%.5f"%(hit / (All * 1.0)))

def Precision(train, test, W, N):
	hit = 0
	All = 0
	for user in train.keys():
		if user not in test.keys():
			continue
		testItems = test[user]
		rank = GetRecommendation(train, user, W, N)
		for item, pui in rank.items():
			if item in testItems:
				hit += 1
		All += N

	return float("%.5f"%(hit / (All * 1.0)))

def Popularity(train, test, W, N):
	item_popularity = dict()
	for user, items in train.items():
		for item in items:
			if item not in item_popularity:
				item_popularity[item] = 0
			item_popularity[item] += 1
	#pprint.pprint(item_popularity)

	ret = 0
	p = 0
	for user in train.keys():
		rank = GetRecommendation(train, user, W, N)
		for item, pui in rank.items():
			if item not in item_popularity:
				continue
			p += math.log(1 + item_popularity[item])
			ret += 1

	return float("%.5f"%(p / ( ret * 1.0 )))

# 计算平均流行度时对每个物品的流行度取对数，
# 因为物品的流行度分布满足长尾分布，在取对数后，流行度的平均值更加稳定

def Coverage(train, test, W, N):
	recommend_items = set()
	all_items = set()

	for user in train.keys():
		for item in train[user]:
			all_items.add(item)

		rank = GetRecommendation(train, user, W, N)
		for item, pui in rank.items():
			recommend_items.add(item)

	return float("%.5f"%(len(recommend_items) / (len(all_items) * 1.0)))



def ItemSimilarity(train):
	# 计算共现矩阵
	N = {}
	C = {}

	for u, items in train.items():
		for i in items:
			N[i] = N.get(i, 0) + 1

			if i not in C.keys():
				C[i] = {}
			for j in items:
				if i == j:
					continue
				C[i][j] = C[i].get(j, 0) + 1
	# 计算最终相似度
	# W = {}
	# for i, related_items in C.items():
	# 	if i not in W.keys():
	# 		W[i] = {}
	# 	for j, cij in related_items.items():
			
	# 		W[i][j] = float("%.3f"% (cij / math.sqrt(N[i] * N[j] * 1.0)))

	# return W
	return C

def GetRecommendation(train, user, W, K):
	rank = {}
	trainItems = train[user]
	pi = 1.0
	for i in trainItems:
		for j , wj in sorted(W[i].items(), key = operator.itemgetter(1), reverse=True)[0:K]:
			#if j in trainItems:
				#continue
			rank[j] = rank.get(j, 0) + pi * wj
			#rank[j].reason[i] = pi * wj

	return rank

def GenericRecommendationList(train, W, K):
	with open("recommendation.txt", 'w') as rec:
		for user in train.keys():
			rank = GetRecommendation(train, user, W, K)
			
			rec.write("{0}\t".format(user))
			topN = sorted(rank, key = lambda x: rank[x], reverse = True)
			for item in topN:
				rec.write("{0}:{1}\t".format(item, rank[item]))
			rec.write("\n")


def GetInvertedList(data):
	ret = {}
	for user, item in data:
		if user not in ret.keys():
			ret[user] = []
		if item in ret[user]:
			continue
		ret[user].append(item)

	return ret

def GetData():
	reader = csv.reader(sys.stdin, delimiter="\t")
	next(reader, None)

	data = []
	for line in reader:
		if len(line) != 2:
			continue
		user = line[0]
		items = line[1].translate(None, string.punctuation).split()
		for item in items:
			data.append([user, item])

	return data


def main():
	data = GetData()
	train = GetInvertedList(data)
	W = ItemSimilarity(train)
	GenericRecommendationList(train, W, 10)
	
	# M = 8
	# recall = 0.0
	# precision = 0.0
	# cover = 0.0
	# popu = 0.0
	# for k in range(M):
	# 	seed = 1000
	# 	train, test = splitData(data, k, M, seed)

	# 	# get inverted list
	# 	train = GetInvertedList(train)
	# 	test = GetInvertedList(test)
	# 	#pprint.pprint(train)
	# 	#pprint.pprint(test)

	# 	W = ItemSimilarity(train)
	# 	#pprint.pprint(W)

	# 	topK = 20# 3, 5, 10, 20
	# 	recall += Recall(train, test, W, topK)
	# 	precision += Precision(train, test, W, topK)
	# 	cover += Coverage(train, test, W, topK)
	# 	popu += Popularity(train, test, W, topK)

	# print recall/M, precision/M, cover/M, popu/M


if __name__ == '__main__':
	main()



