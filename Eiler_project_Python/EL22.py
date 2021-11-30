import os, sys

name_file = "names.txt"

def count(name):
	letters = [ord(x)-96 for x in name.lower()]
	return sum(letters)

with open(os.path.join(sys.path[0], name_file), "r") as f:
	data = f.read()
	data = data.replace('"', '').split(',')
	data.sort()

scores = 0
for i in range(len(data)):
	scores += count(data[i]) * (i + 1)

print(scores)

