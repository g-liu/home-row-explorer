import sys
import fileinput

# Returns the number of words in the top n most frequently used words
def numInTop(n):
	f = open(sys.argv[1], 'r')
	numInTop = 0
	for i in range(0, n):
		word = f.readline().strip().split("\t")[0]
		if word in word_list:
			numInTop += 1

	f.close()
	return numInTop

if len(sys.argv) != 4:
	print("Usage: py rowstats.py <word-freq-file> <word-list> <top-n-count>")
	exit(len(sys.argv))

word_list = set(line.strip() for line in open(sys.argv[2]))

print(numInTop(int(sys.argv[3])))
