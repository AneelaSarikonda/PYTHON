class Computer:
	def __init__(self):
		self.name="Anee"
		self.age=22

	def update(self):
		self.age=27
	
	def compare(self,other):
		if self.age==other.age:
			return True
		else:
			return False

c1=Computer()
c2=Computer()

c1.name="Ajuuu"
c1.age=26

c1.update()

print(c1.name,c1.age,c2.name,c2.age)


if c1.compare(c2):
	print("Age is same")
