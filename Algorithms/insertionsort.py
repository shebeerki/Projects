lis = input("enter the list\n")
lim = len(lis)
p = 0

def swap(lis, a, b):
	lis[a], lis[b] = lis[b], lis[a]
	return 0

def swap_more(lis, k, l):
	for h in range(k, l, -1):
		swap(lis, h, h-1)
	return lis

for i in range(lim):
	pre = lis[i]
	for j in range(i-1, 0, -1):
		if pre < lis[j] and j <> 0:
			pass
		else:
			swap_more(lis, i, j+2)
			p = j 
	swap(lis, i, p)

print "the sorted list is %r\n"%lis
