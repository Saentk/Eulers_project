x = 1
num = '0'
while len(num) <= 1000000:
    num += str(x)
    x += 1

ls = [1,10,100,1000,10000,100000,1000000]
sum = 1
for i in ls:
    sum *= int(num[i])
print(sum)