
fibonacci = [0, 1]
while True:
	new_number = fibonacci[-1] + fibonacci[-2]
	if new_number >= 4000000:
		break
	fibonacci.append(new_number)

print(sum([x for x in fibonacci if x % 2 == 0]))


# I wrote the code below in the first week of learning programming, I'll keep it as a keepsake)
# It works right, but looks awful)

# numbers = []
# i = 0
# x = 1
# while i < 3999999:
# 	i = i + x
# 	print(i)
# 	if i % 2 == 0:
# 		numbers.append(i)
# 	if i > 3999999:
# 		break
# 	x = x + i
# 	if x % 2 == 0:
# 		numbers.append(x)
# 	if x > 3999999:
# 		break
# 	print(x)

# print("Result is ", sum(numbers))