def smallest_factor(arg):
    num = arg
    while True:
        for j in range(arg, 0, -1):
            if num % j != 0:
                break
            if j == 1:
                return num
        num += arg

print(smallest_factor(20))
