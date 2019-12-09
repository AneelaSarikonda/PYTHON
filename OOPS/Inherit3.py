class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
x = Derived()  
print(x.Summation(10,20))  
print(x.Multiplication(10,20))  
print(x.Divide(10,20))  
print(issubclass(Derived,Calculation1))
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))
print(isinstance(x,Derived))
