fib = [0,1]

i = 2
stop_number = 10**999
while True:
	fib_new = fib[i-1]+fib[i-2]
	fib.append(fib_new)
	if fib_new>stop_number:
		print(i)
		break
	i += 1


# def solution(n):
# 	return math.ceil(4.78497 * n - 3.1127)

# print(solution(1000))