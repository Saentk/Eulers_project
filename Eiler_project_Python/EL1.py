numbers = []
numbers1 = []
x = 1
y = 1
while x < 999:
	x = x + 1
	if x % 3 == 0:
		numbers.append(x)
	if x % 5 == 0:
		numbers.append(x)
while y < 999:
	y = y + 1
	if y % 15 == 0:
		numbers1.append(y)
Result = sum(numbers) - sum(numbers1)
print(Result)

