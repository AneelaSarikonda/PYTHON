class Student:
	

	def __init__(var,m1,m2,m3):
		var.m1=m1
		var.m2=m2
		var.m3=m3


	def avg(s):
		return (s.m1 + s.m2 + s.m3)/3



s1=Student(36,57,89)
s2=Student(46,60,27)

print(s1.avg())
print(s2.avg())

