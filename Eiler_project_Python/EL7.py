
import math

def is_prime(num):
	n = round(math.sqrt(num))
	for x in range(2, n + 1):
		if num % x == 0:
			return False
	return True

prime_nums = []
j = 2
while len(prime_nums) < 10001:
	if is_prime(j):
		prime_nums.append(j)
	j += 1
print(prime_nums[-1])