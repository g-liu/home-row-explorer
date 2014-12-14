import sys

if len(sys.argv) != 3:
	print('Usage: python homerow.py <dictionary> <layout>')
	print('  <layout>: one of "q" (QWERTY) or "d" (Dvorak)')
	exit(len(sys.argv))

home = set('asdfghjkl;\'') if sys.argv[2] is "q" else set('aoeuidhtns-')

for line in open(sys.argv[1], 'r'):
	line = line.strip();
	if set(line.lower()) <= home:
		print(line)
