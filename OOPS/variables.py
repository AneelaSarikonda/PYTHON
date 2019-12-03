class Car:
	wheels=4

	def __init__(self):
		self.mil=20
		self.model="BMW"

c1=Car()
c2=Car()

c1.mil=40
Car.wheels=6
print(c1.mil,c1.model,c2.mil,c2.model)
print(Car.wheels)
