
def find_d(num):
	list = []
	for x in range(1, num):
		if num % x == 0:
			list.append(x)
	return sum(list)

data_dict = {}

for number in range(10000):
	d_number = find_d(number)
	if d_number == 1 or d_number == number:
		continue
	data_dict[number] = d_number

done = []
for x in data_dict.items():
	number, d_number = x
	if number in done:
		continue
	candidate = data_dict.get(d_number)
	if candidate == number:
		print(number, '--', d_number)
		done.append(d_number)


