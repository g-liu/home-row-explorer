import sys
import fileinput

def getLengthDistribution(wordList):
	lengths = dict()

	for word in wordList:
		lengths[len(word)] = 1 if len(word) not in lengths else lengths[len(word)] + 1

	return lengths

print(getLengthDistribution(fileinput.input()))
