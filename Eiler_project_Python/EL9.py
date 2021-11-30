
def Pifagor(n):
    for a in range(1, n):
        for b in range(a, n // 2):
            for c in range(b, n // 2):
                if a + b + c == 1000:
                    if a ** 2 + b ** 2 == c ** 2:
                        result = a * b * c
                        return result, (a, b, c)


print(Pifagor(1000))
