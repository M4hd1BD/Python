def binary_search(n,list,l,h):
	if l > h:
		print("Not Found")
	m = int((l + h) / 2)
	if n == list[m]:
		print("Found it, it is at",m)
	elif n > list[m]:
		return binary_search(n,list,m+1,h)
	else:
		return binary_search(n,list,l,m-1)
list = [int(x) for x in input("Enter the list: ").split()]
n = int(input("Number to search: "))
l = 0
h = len(list) - 1
binary_search(n,list,l,h)