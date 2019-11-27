from functools import reduce
nums=[3,8,4,10,2,6,5,7]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,nums))
sums=reduce(lambda a,b : a+b,doubles)
print(evens)
print(doubles)
print(sums)

def is_even(n):
	return n%2==0

def update(n):
	return n*2


def addall(a,b):
	return a+b


