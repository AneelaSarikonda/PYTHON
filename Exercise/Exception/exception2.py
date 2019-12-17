'''a=10
b=0
c=a/b
print(c)'''
try:  
	a = 10  
	b = 0
	print(a/b)
    
except:  
	print("can't divide by zero")  

"""except:
    print("Name Error:d,e,f variables are not defined")


except:
    print("Indentation Error")


except:

    print("IOError: File not found")"""

else:  
	print("Hi I am else block")   
finally:
	print("final")
