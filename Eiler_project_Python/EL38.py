
def is_pandigit(num):
	ls = set(range(1,10))
	if set([int(x) for x in str(num)]) == ls:
		return True

def find_pandigit(num):
	digit = ''
	x = 1
	while len(digit) <= 9:
		result = num * x
		digit += str(result)
		if len(digit) == 9 and is_pandigit(digit): 
			return int(digit)
		x += 1
	return False

max_value = 0
for i in range(1,10000):
	value = find_pandigit(i)
	if value:
		if max_value < value:
			max_value = value

print(max_value) # 932718654 

