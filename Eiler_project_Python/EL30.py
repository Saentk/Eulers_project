list_of_numbers = []
for x in range(2, 5*9**5+1):
    summ = 0
    for i in str(x):
        summ += int(i) ** 5
    if summ == int(x):
        list_of_numbers.append(int(x))

print(list_of_numbers)
print(sum(list_of_numbers))
