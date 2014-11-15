import sys

homeQWERTY = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'];
homeDVORAK = ['a', 'o', 'e', 'u', 'i', 'd', 'h', 't', 'n', 's'];

if len(sys.argv) != 2:
	print('Usage: python homerow.py <dictionary>')
	exit(len(sys.argv))

matchesQWERTY = list()
matchesDvorak = list()

for line in open(sys.argv[1]):
	canAdd = {"Q": True, "D": True}
	for ch in line.strip().lower():
		if ch not in homeQWERTY:
			canAdd["Q"] = False
		if ch not in homeDVORAK:
			canAdd["D"] = False
		if not canAdd["Q"] and not canAdd["D"]:
			break

	if canAdd["Q"]:
		matchesQWERTY.append(line.strip())
	if canAdd["D"]:
		matchesDvorak.append(line.strip())

print(matchesQWERTY)
print()
print(matchesDvorak)
