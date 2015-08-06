#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def Coverage(train, test, N):
	recommend_items = set()
	all_items = set()

	for user in train.keys():
		for item in train[user].keys():
			all_items.add(item)

		rank = GetRecommendation(user, N)
		for item, pui in rank:
			recommend_items.add(item)

	return len(recommend_items) / (len(all_items) * 1.0)

