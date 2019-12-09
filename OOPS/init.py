class Computer:

	def __init__(m,cpu,ram):
		m.cpu=cpu
		m.ram=ram

	def config(m):
		print("config is",m.cpu,m.ram)
	def xam(s):
		print("hiii")
com1=Computer('i5',16)
com2=Computer('Ryzen 3',8)

com1.config()
com2.config()
com1.xam()
print(getattr(com1,'ram'))
setattr(com1,"ram",46)
com1.config()
delattr(com1,'cpu')
com2.config()
print(hasattr(com1,'cpu'))
print(com1.__module__)
