# ~20 sec
def find_sides(p):
    count = 0
    for c in range(p//3, p//2):
        for b in range(1, p//2):
            a = p - b - c
            if a**2 + b**2 == c**2:
                count += 1
    return count / 2


max_value = {'value': 0, 
             'number0': 0}

for p in range(1, 1000):
    new_num = find_sides(p)
    if new_num > max_value['value']:
        max_value['value'] = new_num
        max_value['number'] = p

print(max_value['number'])