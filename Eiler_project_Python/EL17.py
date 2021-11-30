list_str_numbers = []
d = {
	0 : '',
	1 : 'one',
	2 : 'two',
	3 : 'three',
	4 : 'four',
	5 : 'five',
	6 : 'six',
	7 : 'seven',
	8 : 'eight',
	9 : 'nine',
	10 : 'ten',
	11 : 'eleven',
	12 : 'twelve',
	13 : 'thirteen',
	14 : 'fourteen',
	15 : 'fifteen',
	16 : 'sixteen',
	17 : 'seventeen',
	18 : 'eighteen',
	19 : 'nineteen',
	20 : 'twenty',
	30 : 'thirty',
	40 : 'forty',
	50 : 'fifty',
	60 : 'sixty',
	70 : 'seventy',
	80 : 'eighty',
	90 : 'ninety',
	100 : 'one hundred',
}

for x in range(1, 1001):
	x = str(x)
	z1 = int(x[-1])
	res1 = d.get(z1)
	if len(x) == 1:
		list_str_numbers.append(res1)
	elif len(x) == 2:
		if int(x[-2:]) < 20:
			res_exception = d.get(int(x[-2:]))
			list_str_numbers.append(res_exception)
		else:
			z2 = int(x[-2]) * 10
			res2 = d.get(z2) + ' ' + res1
			list_str_numbers.append(res2)
	elif len(x) == 3:
		if int(x[-3:]) % 100 == 0:
			if int(x) == 100:
				list_str_numbers.append(d.get(100))
			else:
				res3 = d.get(int(x[-3])) + ' hundreds'
				list_str_numbers.append(res3)
		elif int(x[-3]) == 1:
			if int(x[-2:]) < 20:
				res_exception = d.get(int(x[-2:]))	
				res3 = d.get(100) + ' and ' +  res_exception
				list_str_numbers.append(res3)
			else:
				z2 = int(x[-2]) * 10
				res2 = d.get(z2) + ' ' + res1
				res3 = d.get(100) + ' and ' + res2
				list_str_numbers.append(res3)
		else:
			if int(x[-2:]) < 20:
				res_exception = d.get(int(x[-2:]))	
				res3 = d.get(int(x[-3])) + ' hundreds' + ' and ' +  res_exception
				list_str_numbers.append(res3)
			else:
				z2 = int(x[-2]) * 10
				res2 = d.get(z2) + ' ' + res1
				res3 = d.get(int(x[-3])) + ' hundreds' + ' and ' + res2
				list_str_numbers.append(res3)

list_str_numbers.append('one thousand')
summ = 0
for x in list_str_numbers:
	x = x.replace(' ', '')
	summ += len(x)

print(summ)