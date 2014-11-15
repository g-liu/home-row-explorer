import sys

homeQWERTY = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'];
homeDVORAK = ['a', 'o', 'e', 'u', 'i', 'd', 'h', 't', 'n', 's'];

if len(sys.argv) != 2:
	print('Usage: python homerow.py <dictionary>')
	exit(len(sys.argv))

matchesQWERTY = set()
matchesDvorak = set()

for line in open(sys.argv[1]):
	canAdd = {"Q": True, "D": True}
	for ch in line.strip().lower():
		if ch not in homeQWERTY:
			canAdd["Q"] = False
			break
		if ch not in homeDVORAK:
			canAdd["D"] = False
			break

	if canAdd["Q"]:
		matchesQWERTY.add(line.strip())
	if canAdd["D"]:
		matchesDvorak.add(line.strip())

print(matchesQWERTY)
print(matchesDvorak)
