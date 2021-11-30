import calendar

list1 = []

for y in range(1901, 2001):
	for m in range(1, 13):
		alc = calendar.monthrange(y, m)
		list1.append(alc)

y = 0
for x, z in list1:
	if x == 6:
		y = y + 1

print(y)