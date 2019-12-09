class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		"""This is in fun"""
		print('Hello')
	
x=MyClass()
x.func()
print(MyClass.a)

#print(MyClass.func)

print(MyClass.__doc__)
print(x.func.__doc__)
