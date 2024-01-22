# def simpleGeneratorFun():
#     yield 2
#     yield 3
#     yield 4
# x=simpleGeneratorFun()
# print(next(x))
# print(next(x))
# print(next(x))


# def square_generator(n):
#     for i in range(n):
#         yield i**2
# n_values=5
# squares=square_generator(n_values)
# for square in squares:
#     print(square)

#generators
    

# def make_pretty(func):
#     def inner():
#         print("i got decorated")
#         func()
#     return inner
# @make_pretty
# def ordinary():
#     print("I am ordinary")
# ordinary()

# def ensure_positive_integer(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, int) and result > 0:
#             return result
#         else:
#             print("Error: Result is not a positive integer. Setting result to 1.")
#             return 1
#     return wrapper

# @ensure_positive_integer
# def multiply(a, b):
#     return a * b

# @ensure_positive_integer
# def subtract(x, y):
#     return x - y

# result_multiply = multiply(5, 3)
# result_subtract = subtract(10, 7)

# print("Result of multiply:", result_multiply)
# print("Result of subtract:", result_subtract)



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print("Factorial of 5 is:", result)

#recursion

    