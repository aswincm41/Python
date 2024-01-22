# def add(a,b):
#     print(a+b)
# add(5,7)

# def add(a,b):
#     print(a+b)
# add(5,5)

# def add(a,b):
#     return a+b
# x=int(input("enter the number1:"))
# y=int(input("enter the number2:"))
# print(add(x,y))

# def add(a,b):
#     return a+b
# x=(input("enter the first name:"))
# y=(input("enter the last name:"))
# print(add(x,y))

#function using def


# def power(base,exponent=2):
#     return base**exponent
# result1=power(2)
# result2=power(2,3)
# print("result1:",result1)
# print("result2:",result2)


# def greet(first_name, last_name):
#     print('First Name:', first_name)
#     print('Last Name:', last_name)
# # Calling the function with keyword arguments
# greet(last_name='Cartman', first_name='Eric')

# def greet(name,greeting):
#     print(f"{greeting},{name}!")
# greet("aswin","hello")


# def myFun(*argv):
#     for arg in argv:
#         print(arg)
# # Calling the function with multiple arguments
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# def func(*argv):
#     for arg in argv:
#         print(arg)
# func("hi","aswin","how","are","you")
#argv


# def func(**kwargs):
#     d = {}
#     for key, value in kwargs.items():
#         d[key] = value
#     print(d)

# func(first='hello', mid='guys', last='welcome back')
#kwargs



#different types of function arguments



# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3

# # x is a generator object
# x = simpleGeneratorFun()

# # Iterating over the generator object using next
# print(next(x))
# print(next(x))
# print(next(x))


# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# # Calling the decorated function
# ordinary()
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Additional code to be executed before the original function
        print("Something is happening before the function is called.")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Additional code to be executed after the original function
        print("Something is happening after the function is called.")
        
        return result
    return wrapper

# Applying the decorator to a function
@my_decorator
def my_function():
    print("I am the original function.")

# Calling the decorated function
my_function()


