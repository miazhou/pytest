def func(r):
	t1=sum([i**2 for i in r])
	t2=sum(r)**2
	return t2-t1

print func(range(1,11))
		
