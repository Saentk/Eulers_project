from math import factorial

def find_factorial(num):
	fac = 1
	for x in range(1, num+1):
		fac *= x     # don`t want to import math.factorial for simple job
	return fac


def find_sum_of_number(num):
	res = 0
	for i in str(num):
		res += int(i)
	return res

print(find_sum_of_number(find_factorial(100)))
