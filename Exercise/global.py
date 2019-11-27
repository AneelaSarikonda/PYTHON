a=10


def fun():
	global a           # To change global variable use the global keyword
	a=20
	print("Inside fun:",a)


fun()


print("outside fun:",a)
