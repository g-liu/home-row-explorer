import sys
from math import floor
from pprint import pprint

def printHomeRowWords():
	for line in open(sys.argv[1], 'r'):
		line = line.strip()
		if set(line.lower()) <= home:
			print(line)

def getHomeRowHistogram():
	""" Runs through all words in dictionary file,
	    for each word, determines what percentage of its
	    letters belong on the home row. Creates histogram
	    out of this data. """
	histo = {i: 0 for i in range(0, 100)}
	for line in open(sys.argv[1], 'r'):
		charsOnHome = 0
		line = line.strip()
		for ch in line:
			if ch in home:
				charsOnHome += 1
		
		perc = round(charsOnHome / len(line) * 100)
		histo[perc] = histo[perc] + 1 if perc in histo else 1

	return histo

def bucketize(histo, size):
	""" Takes the home row histogram, which is quantized by 1,
	    and outputs a new dict quantized by the given size """
	if size == 1:
		return histo

	bucket = dict()
	for i in range(0, floor(100/size)*size+1, size):
		tally = 0
		for j in range(i, min(i + size, 101)):
			tally += histo[j]
		bucket[i] = tally

	if i <= 100:
		stopped = i
		tally = 0
		for i in range(stopped, 101):
			tally += histo[i]
		bucket[stopped] = tally

	return bucket


if len(sys.argv) < 4:
	print('Usage: python homerow.py <dictionary> <layout> <h|w>')
	print('  <layout>: one of "q" (QWERTY) or "d" (Dvorak)')
	print('  <h|w>: h to print histogram, w for word list')
	exit(len(sys.argv))

home = set('asdfghjkl;\'') if sys.argv[2] is "q" else set('aoeuidhtns-')

if sys.argv[3].lower() == 'h':
	bucketSize = int(sys.argv[4]) if len(sys.argv) >= 5 else 1
	histo = bucketize(getHomeRowHistogram(), bucketSize)
	pprint(histo)
elif sys.argv[3].lower() == 'w':
	printHomeRowWords()
