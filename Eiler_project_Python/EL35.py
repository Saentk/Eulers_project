# ~5 sec
# I`m not sure I did it right)
import math as m
import time

def is_simple(numb):
	n = round(m.sqrt(numb))
	for divider in range(2, n+1):
		if numb % divider == 0:
			return False
	return True

def circular_prime(numb): 
	numbers_list = [x for x in str(numb)]
	for x in numbers_list:
		if int(x) % 2 == 0:
			return False
	for x in range(len(numbers_list)):
		new_number = ''
		numbers_list.append(numbers_list.pop(0))
		for x in numbers_list:
			new_number += x
		if is_simple(int(new_number)) == False:
			return False
	return True


start = time.time()

final_list = []
for numb in range(3, 1000000, 2):
	if is_simple(numb):
		if circular_prime(numb):
			final_list.append(numb)
print(len(final_list))

print('time = ', time.time() - start)


