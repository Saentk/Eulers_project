# ~4sec

done = {}
def count_Collatz(num):
	cycles = 0
	while num > 1:
		if num in done:
			return cycles + done[num]
		if num % 2 == 0:
			num /= 2
		else:
			num = num * 3 + 1
		cycles += 1
	return cycles + 1


max_value = value = 0
for num in range(2, 1000000):
	cycles = count_Collatz(num)
	done[num] = cycles
	if max_value < cycles:
		max_value = cycles
		value = num

print('value = ', value,'cycles = ', max_value)

