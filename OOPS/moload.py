class A:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		

# adding two objects  
	def sum(self): 
		return self.a + self.b  
ob1 = A(1,3)
#ob2 = A(6) 
ob3 = A("Geeks","Hii") 
#ob4 = A("For") 
print(ob1+ob3)  
print(ob1.sum()) 
print(ob3.sum()) 

