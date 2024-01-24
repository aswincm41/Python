# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius
# class Square(Shape):
#     def __init__(self,side_length):
#         self.side_length=side_length
#     def area(self):
#         return self.side_length**2
#     def perimeter(self):
#         return 4* self.side_length
# circle= Circle(radius=4)
# square= Square(side_length=4)
# print("Circle -area:", circle.area(),"Perimeter:",circle.perimeter())
# print("square-area:",square.area(),"Perimeter:",square.perimeter)     

# from abc import ABC , abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     def perimeter(self):
#         pass
# class triangle(Shape):
#     def __init__(self,base,height,side1,side2,side3):
#         self.base= base
#         self.height=height
#         self.side1=side1
#         self.side2=side2
#         self.side3=side3
#     def area(self):
#         return 0.5*self.base*self.height
#     def perimeter(self):
#         return self.side1 + self.side2 +self.side3
# class Rectangle(Shape):
#     def __init__(self,lenght,width):
#         self.lenght= lenght
#         self.width= width
#     def area(self):
#         return self.lenght *self.width
#     def perimeter(self):
#         return 2*(self.lenght+self.width)
# triangle_instance =triangle(base=5,height=3,side1=3,side2=4,side3=5)
# rectangle_instance=Rectangle(lenght=3,width=5)
# print("Triangle - Area:", triangle_instance.area(), "Perimeter:", triangle_instance.perimeter())
# print("Rectangle - Area:", rectangle_instance.area(), "Perimeter:", rectangle_instance.perimeter())

#ABSTACT METHOD


# class MathOperators:
#     @staticmethod
#     def add(x,y):
#         return x+y
#     @staticmethod
#     def subtract(x,y):
#         return x-y
# result_add=MathOperators.add(5,3)
# result_subtract=MathOperators.subtract(9,4)
# print("result of addition:",result_add)
# print("result of subtraction:",result_subtract)




# class MathOperators:
#     @staticmethod
#     def mul(a,b):
#         return a*b
#     @staticmethod
#     def div(a,b):
#         return a/b
# result_multiply=MathOperators.mul(5,3)
# result_division=MathOperators.div(15,3)
# print("result of multiplication:",result_multiply)
# print("result of division:",result_division)


#static method


# class Myclass:
#     class_variable="I am a class variable"
#     @classmethod
#     def print_class_variable(cls):
#         print(cls.class_variable)
# Myclass.print_class_variable()


# class MathOperations:
#     @classmethod
#     def add(cls, x, y):
#         print(f"Performing addition using class method ({cls.__name__})")
#         return x + y
#     @classmethod
#     def multiply(cls, x, y):
#         print(f"Performing multiplication using class method ({cls.__name__})")
#         return x * y
# result_add = MathOperations.add(5, 3)
# result_multiply = MathOperations.multiply(4, 5)
# print("Result of addition:", result_add)
# print("Result of multiplication:", result_multiply)


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
instance1 = Counter()
instance2 = Counter()
instance3 = Counter()
print("Number of instances created:", Counter.count)
