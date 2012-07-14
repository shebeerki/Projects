
def swap(lis, a, b):
	lis[a],lis[b] = lis[b], lis[a]
	return 0

def smallest(pre, i, j):
	mini = lis[pre]
	for k in range(i, j):
		if lis[pre] > lis[k]:
			mini = lis[k]
		else:
			pass
	return mini

lis = input("enter the list\n")
lim = len(lis) 

for l in range(lim):
	minimum = smallest(l, l+1, lim)
	min_index = lis.index(minimum)
	swap(lis, l, min_index)

print "the sorted list is %r"%lis
