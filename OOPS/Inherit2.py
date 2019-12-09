class Animal:  
    def speak(self):  
        print("Animal Speaking")  

class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
  
#class Puppy(Dog,Animal):  
class Puppy(Dog):
    def eat(self):  
        print("Eating bread...")  
d = Puppy()  
d.bark()  
d.speak()  
d.eat()  
print(issubclass(Dog,Animal))
print(issubclass(Puppy,Dog))
print(isinstance(d,Animal))
