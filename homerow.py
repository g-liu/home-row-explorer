import sys

homeQWERTY = set('asdfghjkl');
homeDVORAK = set('aoeuidhtns');

if len(sys.argv) != 2:
	print('Usage: python homerow.py <dictionary>')
	exit(len(sys.argv))

matchesQWERTY = list()
matchesDvorak = list()

for line in open(sys.argv[1]):
	line = line.strip().lower()

	if set(line) <= homeQWERTY:
		matchesQWERTY.append(line)
	if set(line) <= homeDVORAK:
		matchesDvorak.append(line)

print(matchesQWERTY)
print()
print(matchesDvorak)
