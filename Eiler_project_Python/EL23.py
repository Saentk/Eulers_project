# ~8.2 sec

import math
numb = 28124

list_result = list(range(1, numb))
n_list = []

num = 1
while num < numb:
	num += 1
	total = 0
	n = math.ceil(math.sqrt(num))
	for x in range(2, n):
		if num % x == 0:
			total = total + x
			total = total + num // x
	if n ** 2 == num:
		total = total + n
	if num < total:
		n_list.append(num)


sums = [0]*numb
for x in range (0, len(n_list)):
    for y in range (x, len(n_list)):
            sum_of_abundant_numbers = n_list[x]+n_list[y]
            if sum_of_abundant_numbers < numb:
                if (sums[sum_of_abundant_numbers] == 0):
                    sums[sum_of_abundant_numbers] = sum_of_abundant_numbers

total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        total +=x

print(total)