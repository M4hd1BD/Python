list = [int(x) for x in input().split()]
l = len(list)
check = 1
while check != 0:
	check = 0
	for i in range(0,l-1,1):
		if list[i] > list[i+1]:
			temp = list[i]
			list[i] = list[i+1]
			list[i+1] = temp
			check = check + 1
print(list)