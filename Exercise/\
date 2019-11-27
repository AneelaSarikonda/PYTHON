a=5
print(id(a))


def fun():

	a=9
	x=globals()['a']
	print(id(x))
	
	print("in fun",a)
	globals()['a']=12

fun()
print("outside fun:",a)
