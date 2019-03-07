list = [int(x) for x in input().split()]
print(list)
l = len(list)
for i in range(0,l,1):
	index = 0
	smallest = list[i]
	for j in range(i,l,1):
		if list[j] < smallest:
			smallest = list[j]
			index = j
			temp = list[i] #4
			list[i] = smallest
			list[index] = temp
print(list)