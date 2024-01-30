class Myclass:
    variable="blah"
    def function(self):
        print("This is a message inside the class.")
myobjectx=Myclass()
print(myobjectx.variable)
myobjectx.function()

#class



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"
    
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

print(dog_instance.speak())
print(cat_instance.speak())

#example2


class Animal:
    def __init__(self, name):
      self.name=name
    def speak(self):
          print(f"{self.name}make a sound.")

class Dog(Animal):
   def bark(self):
        print(f"{self.name}barks: woof!")

animal_instance =Animal("Generic Animal")
dog_instance=Dog("Buddy")
animal_instance.speak()
dog_instance.speak()
dog_instance.bark()


      
#SINGLE INHERITANCE

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")
class WingedAnimal:
    def Winged_animal_info(self):
        print("Winged animals can flap.")
class Bat(Mammal,WingedAnimal):
    def bat_info(self):
        super().mammal_info()
        super().Winged_animal_info()
        print("Bats are a combination of mammals and winged animals.")
b1=Bat()
b1.bat_info()


#Example 2

class Mammal:
    def give_birth(self):
        print("mammals give direct birth.")
class WingedAnimal:
    def flap(self):
        print("Winged animals can flap their wings.")
class Bat(Mammal, WingedAnimal):
    def fly(self):
        print("Bats can fly by flapping their wings.")
bat_instance = Bat()

bat_instance.give_birth()
bat_instance.flap()
bat_instance.fly()



#multiple inheritannce
 
class Parent:
    def __init__(self,name):
        self.name= name
    def getName(self):
        return self.name
class Child(Parent):
    def __init__(self, name,age):
        Parent.__init__(self,name)
        self.age=age
    def getAge(self):
        return self.age
class Grandchild(Child):
    def __init__(self, name, age,location):
        Child.__init__(self,name,age)
        self.location=location
    def getLocation(self):
        return self.location
gc=Grandchild("Aswin",23,"kerala")
print(gc.getName())
print(gc.getAge())
print(gc.getLocation())

# Multilevel Inheritance in Python 
