try:
#	fp = open("xyz.txt","r")
	a=35
	b=0
	print(a/b)
	print("This is Exception")
#	d=e+f
except TypeError as d:
	print(d)

except ZeroDivisionError:
	print("IOError: File not found")

else:
	print("This is else block")


finally:
	print("This is Final block")





















