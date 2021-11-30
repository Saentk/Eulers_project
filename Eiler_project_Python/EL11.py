import math

file_name = 'digits.txt'

big_data = []
data_list = []

with open(file_name) as file:
	for x in file:
		big_data.append(x)

for x in big_data:
	i = x.replace('\n', '').split()
	for z in i:
		data_list.append(int(z))


new_lst = [data_list[i:i+20] for i in range(0, len(data_list), 20)]
#print(new_lst) 					 => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def vertical():
	list = []
	for y in range(20):
		for x in range(20 - 3):
			s = new_lst[y][x] * new_lst[y][x + 1] * new_lst[y][x + 2] * new_lst[y][x + 3]
			r = new_lst[y][x], new_lst[y][x + 1], new_lst[y][x + 2], new_lst[y][x + 3]
			d = [s, r]
			list.append(d)
	return max(list)


def gorizontal():
	list = []
	for y in range(20 - 3):
		for x in range(20):
			s = new_lst[y][x] * new_lst[y + 1][x] * new_lst[y + 2][x] * new_lst[y + 3][x]
			r = new_lst[y][x], new_lst[y + 1][x], new_lst[y + 2][x], new_lst[y + 3][x]
			d = [s, r]
			list.append(d)
	return max(list)


def diagonal_right():
	list = []
	for y in range(20 - 3):
		for x in range(20 - 3):
			s = new_lst[y][x] * new_lst[y + 1][x + 1] * new_lst[y + 2][x + 2] * new_lst[y + 3][x + 3]
			r = new_lst[y][x], new_lst[y + 1][x + 1], new_lst[y + 2][x + 2], new_lst[y + 3][x + 3]
			d = [s, r]
			list.append(d)
	return max(list)

def diagonal_left():
	max_value = 0
	for y in range(20 - 3):
		for x in range(3, 20):
			list = [new_lst[y][x], new_lst[y + 1][x - 1], new_lst[y + 2][x - 2], new_lst[y + 3][x - 3]]
			value = math.prod(list)
			if max_value < value:
				max_value = value
				list_of_value = list
	return [max_value, list_of_value]



print(max(vertical(), gorizontal(), diagonal_right(), diagonal_left()))


# r = new_lst[y][x], new_lst[y + 1][x + 1], new_lst[y + 2][x + 2], new_lst[y + 3][x + 3]
# list = [new_lst[y][x], new_lst[y + 1][x - 1], new_lst[y + 2][x - 2], new_lst[y + 3][x - 3]]

# r = new_lst[y][x], new_lst[y + 1][x], new_lst[y + 2][x], new_lst[y + 3][x]
# r = new_lst[y][x], new_lst[y][x + 1], new_lst[y][x + 2], new_lst[y][x + 3]

# max_value = 0
# for y in range(20):
# 	for x in range(20):
# 		try:
# 			axis_x = new_lst[y][x:x+4]
# 		except:
# 			pass
# 		else:
# 			if max_value < math.
# 		

# def find_biggest(fromm, to, value):
# 	max_value = 0
# 	for y in range(fromm):
# 		for x in range(3, to):
# 			list = [new_lst[y][x], new_lst[y + 1][x - 1], new_lst[y + 2][x - 2], new_lst[y + 3][x - 3]]
# 			value = math.prod(list)
# 			if max_value < value:
# 				max_value = value
# 	return max_value