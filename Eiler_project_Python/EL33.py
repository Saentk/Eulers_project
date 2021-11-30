import random as r

def dont_konw_how_to_name_function(x, y):
	if '0' in str(x) or '0' in str(y):
		return False
	for numb in str(x):
		if numb in str(y):
			str_x = str(x).replace(numb, '')
			str_y = str(y).replace(numb, '')
			if str_x and str_y:
				if y / x == int(str_y) / int(str_x): 
					return True

def divmode_division(list):
	numerator = denominator = 1
	for a, b in list:
		numerator *= a
		denominator *= b
	return denominator / numerator

final_list = []
for x in range(11, 100):
	for y in range(11, x):
		if dont_konw_how_to_name_function(x, y):
			final_list.append((y, x))

print(final_list)
print(divmode_division(final_list))
