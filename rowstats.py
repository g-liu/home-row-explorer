import sys
import fileinput

# counts the number of acronyms in the word list
def numAcronyms():
	return sum(1 for line in open(sys.argv[2], 'r') if isAcronym(line))

# counts the number of proper nouns
def numProperNouns():
	return sum(1 for line in open(sys.argv[2], 'r') if isProperNoun(line))

# True or False whether the string given is an acronym
def isAcronym(word):
	return word.isupper()

# True or False whether the string given is a proper noun
def isProperNoun(word):
	return word[0].isupper() and not word.isupper()

# Returns the number of words in the top n most frequently used words
def numInTop(n):
	numInTop = 0
	f = open(sys.argv[1], 'r')
	for i in range(0, n):
		if f.readline().strip().split("\t")[0] in word_list:
			numInTop += 1

	f.close()
	return numInTop

# Counts the number of words in the file
def numWords():
	return sum(1 for line in open(sys.argv[2], 'r') if line.strip())

if len(sys.argv) != 4:
	print("Usage: py rowstats.py <word-freq-file> <word-list> <top-n-count>")
	exit(len(sys.argv))

word_list = set(line.strip() for line in open(sys.argv[2], 'r'))

print("total words: %d" % numWords())
print("--> in top %s: %d" % (sys.argv[3], numInTop(int(sys.argv[3]))))
print("acronyms: %d" % numAcronyms())
print("proper nouns: %d" % numProperNouns())

