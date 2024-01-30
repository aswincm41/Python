class Animal:
    def speak(self):
        print("animal speaks")
class Dog(Animal):
    def speak(self):
        print("dog barks")
class Cat(Animal):
    def speak(self):
        print("cat meow")
dog=Dog()
cat=Cat()
dog.speak()
cat.speak()