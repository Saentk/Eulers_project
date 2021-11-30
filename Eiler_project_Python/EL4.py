
polindroms_list = []
for x in range(999, 101, -1):
	for y in range(999, 101, -1):
		s = x * y
		if str(s) == str(s)[::-1]:
			polindroms_list.append([s, (x, y)])

print(max(polindroms_list))