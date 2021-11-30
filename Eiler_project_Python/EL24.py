import itertools 	

list1 = []
a = '0123456789'     	 
for i in itertools.permutations(a,len(a)):     
	num = (''.join(i))  
	list1.append(num)
	
print(list1[999999])