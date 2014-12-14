import sys

if len(sys.argv) != 3:
	print('Usage: python homerow.py <dictionary> <layout>')
	print('  <layout>: one of "q" (QWERTY) or "d" (Dvorak)')
	exit(len(sys.argv))

matches = list()
home = set('asdfghjkl;\'') if sys.argv[2] is "q" else set('aoeuidhtns-')

for line in open(sys.argv[1]):
	line = line.strip().lower()

	if set(line) <= home:
		print(line)
		matches.append(line)
