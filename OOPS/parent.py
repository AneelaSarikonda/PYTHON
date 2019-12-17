class parent:
	 def __init__(self,sno,name,age):
		self.sno=sno
		self.name=name
                self.age=age



class child(parent):
	def sum(self,sno,name,age):
		#self.id=id
		#self.name=name
		#parent.__init__(sno,name)
		#self.age=age

		print(self.sno,self.name,self.age)


x=child(10,"abc",25)
x.sum()
