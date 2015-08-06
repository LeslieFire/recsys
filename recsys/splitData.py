#!/usr/bin/python

import sys
import string
import csv
import random

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

def splitData(data, k, m, seed):
	test = []
	train = []
	random.seed(seed)
	for user, item in data:
		if random.randint(0, m) == k:
			test.append([user, item])
		else:
			train.append([user, item])

	return train, test

def main():
	M = 8
	seed = 19890910
	data = GetData()
	for k in range(M):
		train, test = splitData(data, k, M, seed)

		# write to file
		trainFile = open("train_data{0}".format(k), 'w')
		for user, item in train:
			trainFile.write("{0}\t{1}\n".format(user, item))
		trainFile.close()

		testFile = open("test_data{0}".format(k), 'w')
		for user, item in test:
			testFile.write("{0}\t{1}\n".format(user, item))
		testFile.close()

if __name__ == '__main__':
	main()
