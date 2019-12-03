class Computer:                         #defining a class
	
	def config(self):		#defining a method
		print("i5,32GB,1TB")


com1=Computer()                         #creates objects
com2=Computer()

Computer.config(com1)		    
Computer.config(com2)
					#calling a method

com1.config()             
com2.config()


