# ~6 sec
import math

def max_triangular(m):
    x = 3; n = 2
    while n <= m:
        n = 2
        num = sum(list(range(1, x+1)))
        sqrt_num = math.ceil(math.sqrt(num))
        for i in range(2, sqrt_num):
            if num % i == 0:
                n += 2
        if sqrt_num ** 2 == num:
                n -= 1
        x += 1
    return num

print(max_triangular(500))


