list = [int (x) for x in input().split()]
l = len(list)
n = int(input("Enter the number you want to search: "))

for i in range(0,l,1):
	if list[i] == n:
		print("%d is in %d no. Index"%(n,i))
		exit()