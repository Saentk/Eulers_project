import math as m

final_list = []
for x in range(3, 100000):
	summ = 0
	for i in str(x):
		summ += m.factorial(int(i))
	if summ == x:
		final_list.append(x)

print(final_list, 'sum =', sum(final_list))