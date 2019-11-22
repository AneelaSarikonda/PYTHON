def sum(a,b):
	return a+b
print(sum(5,6))
del sum
try:
	
	print(sum(5,6))
except TypeError:
	print("Error") 
print("This is Mirafra")

